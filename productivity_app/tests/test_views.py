import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from productivity_app.models import Task, Profile
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user(db):
    return User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="password123"
    )


@pytest.fixture
def auth_client(api_client, create_user):
    """Returns an authenticated client."""
    response = api_client.post(
        reverse("login"),
        {"username": create_user.username, "password": "password123"},
        format="json"
    )
    token = response.data["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client


# --- Authentication Tests ---

def test_user_registration(api_client):
    url = reverse("register")
    data = {
        "username": "newuser",
        "email": "new@example.com",
        "password": "securepass123"
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert "access" in response.data
    assert User.objects.filter(username="newuser").exists()


def test_user_login(api_client, create_user):
    url = reverse("login")
    data = {"username": "testuser", "password": "password123"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data


# --- User API Tests ---

def test_users_list_requires_auth(api_client):
    url = reverse("users-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_users_list_authenticated(auth_client, create_user):
    url = reverse("users-list")
    response = auth_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert any(u["username"] == create_user.username for u in response.data)


def test_user_detail_update(auth_client, create_user):
    url = reverse("user-detail")
    data = {"username": "updateduser"}
    response = auth_client.patch(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    create_user.refresh_from_db()
    assert create_user.username == "updateduser"


# --- Profile API Tests ---

def test_profile_list(api_client, create_user):
    url = reverse("profile-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert any("user" in profile for profile in response.data)


def test_profile_update_only_self(auth_client, create_user):
    profile = create_user.profile
    url = reverse("profile-detail", args=[profile.id])
    data = {"name": "Updated Name"}
    response = auth_client.patch(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    profile.refresh_from_db()
    assert profile.name == "Updated Name"


# --- Task API Tests ---

@pytest.fixture
def create_task(create_user):
    task = Task.objects.create(
        title="Test Task",
        description="Task description",
        due_date=timezone.now().date() + timedelta(days=1),
        priority="medium",
        status="pending",
        created_by=create_user
    )
    task.assigned_users.set([create_user])
    return task


def test_task_list_authenticated(auth_client, create_task):
    url = reverse("task-list")
    response = auth_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert any(task["title"] == "Test Task" for task in response.data)


def test_task_create(auth_client):
    url = reverse("task-list")
    data = {
        "title": "New Task",
        "description": "Some description",
        "due_date": str(timezone.now().date() + timedelta(days=2)),
        "priority": "low",
        "status": "pending"
    }
    response = auth_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Task.objects.filter(title="New Task").exists()


def test_task_update_only_if_assigned(auth_client, create_task):
    url = reverse("task-detail", args=[create_task.id])
    data = {"title": "Updated Task"}
    response = auth_client.patch(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    create_task.refresh_from_db()
    assert create_task.title == "Updated Task"


def test_task_delete_only_if_assigned(auth_client, create_task):
    url = reverse("task-detail", args=[create_task.id])
    response = auth_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Task.objects.filter(id=create_task.id).exists()
