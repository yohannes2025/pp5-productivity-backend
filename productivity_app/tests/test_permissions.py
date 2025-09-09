import pytest
from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.contrib.auth import get_user_model
from productivity_app.models import Task, Profile
from productivity_app.permissions import (
    IsAssignedOrReadOnly,
    IsSelfOrReadOnly,
    IsOwnerOrReadOnly,
)
from django.utils import timezone
from datetime import timedelta

User = get_user_model()


@pytest.fixture
def factory():
    return APIRequestFactory()


@pytest.fixture
def user1(db):
    return User.objects.create_user(username="user1", password="pass123")


@pytest.fixture
def user2(db):
    return User.objects.create_user(username="user2", password="pass123")


@pytest.fixture
def task(user1, user2):
    task = Task.objects.create(
        title="Task A",
        description="Test Task",
        due_date=timezone.now().date() + timedelta(days=1),
        priority="medium",
        status="pending",
        created_by=user1,
    )
    task.assigned_users.set([user1])
    return task


@pytest.fixture
def profile(user1):
    return user1.profile  # auto-created via signal


# --- IsAssignedOrReadOnly ---

def test_is_assigned_or_read_only_allows_safe_methods(factory, user2, task):
    request = factory.get("/")
    request.user = user2
    perm = IsAssignedOrReadOnly()
    assert perm.has_object_permission(request, None, task)


def test_is_assigned_or_read_only_denies_unassigned_edit(factory, user2, task):
    request = factory.patch("/")
    request.user = user2
    perm = IsAssignedOrReadOnly()
    assert not perm.has_object_permission(request, None, task)


def test_is_assigned_or_read_only_allows_assigned_edit(factory, user1, task):
    request = factory.patch("/")
    request.user = user1
    perm = IsAssignedOrReadOnly()
    assert perm.has_object_permission(request, None, task)


# --- IsSelfOrReadOnly ---

def test_is_self_or_read_only_allows_safe_methods(factory, user1, user2):
    request = factory.get("/")
    request.user = user1
    perm = IsSelfOrReadOnly()
    assert perm.has_object_permission(request, None, user2)


def test_is_self_or_read_only_allows_self_edit(factory, user1):
    request = factory.patch("/")
    request.user = user1
    perm = IsSelfOrReadOnly()
    assert perm.has_object_permission(request, None, user1)


def test_is_self_or_read_only_denies_edit_other_user(factory, user1, user2):
    request = factory.patch("/")
    request.user = user1
    perm = IsSelfOrReadOnly()
    assert not perm.has_object_permission(request, None, user2)


# --- IsOwnerOrReadOnly ---

def test_is_owner_or_read_only_allows_safe_methods(factory, user1, profile):
    request = factory.get("/")
    request.user = user1
    perm = IsOwnerOrReadOnly()
    assert perm.has_object_permission(request, None, profile)


def test_is_owner_or_read_only_allows_owner_edit(factory, user1, profile):
    request = factory.patch("/")
    request.user = user1
    perm = IsOwnerOrReadOnly()
    assert perm.has_object_permission(request, None, profile)


def test_is_owner_or_read_only_denies_non_owner_edit(factory, user2, profile):
    request = factory.patch("/")
    request.user = user2
    perm = IsOwnerOrReadOnly()
    assert not perm.has_object_permission(request, None, profile)
