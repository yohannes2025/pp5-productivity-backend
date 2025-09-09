import pytest
from productivity_app.serializers import TaskSerializer, RegisterSerializer
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


def test_task_serializer_valid_data(db, create_user, create_category):
    data = {
        'title': 'Task',
        'description': 'Details',
        'due_date': str(timezone.now().date() + timedelta(days=1)),
        'priority': 'high',
        'category': create_category.id,  # Use the ID of the created category
        'status': 'pending',
        'assigned_users': [create_user.id]
    }
    serializer = TaskSerializer(data=data)
    assert serializer.is_valid()
    instance = serializer.save(created_by=create_user)
    assert instance.assigned_users.first() == create_user


@pytest.mark.django_db
def test_register_serializer_valid_data():
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123!',
        'confirm_password': 'password123!'
    }
    serializer = RegisterSerializer(data=data)
    assert serializer.is_valid()
    user = serializer.save()
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'
    assert user.check_password('password123!')


@pytest.mark.django_db
@pytest.mark.parametrize("field, value", [
    ('password', 'short'),
    ('email', 'test@example.com'),
    ('username', 'existinguser')
])
def test_register_serializer_invalid_data(field, value):
    # Create an existing user if testing for existing fields
    if field in ['email', 'username']:
        User.objects.create_user(
            username='existinguser', email='test@example.com', password='password123!'
        )

    data = {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password': 'password123!',
        'confirm_password': 'password123!'
    }
    data[field] = value
    if field == 'password':
        data['confirm_password'] = value

    serializer = RegisterSerializer(data=data)
    assert not serializer.is_valid()
    assert field in serializer.errors


@pytest.fixture
def create_category(db):
    """Fixture to create a sample category."""
    from productivity_app.models import Category
    return Category.objects.create(name='Development')
