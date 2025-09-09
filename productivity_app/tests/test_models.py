import pytest
from django.utils import timezone
from productivity_app.models import Task, Profile, Category
from datetime import timedelta
from django.core.exceptions import ValidationError


@pytest.fixture
def create_category(db):
    """Fixture to create a sample category."""
    return Category.objects.create(name='Development')


def test_task_creation(db, create_user, create_category):
    task = Task.objects.create(
        title="Sample Task",
        description="Test description",
        due_date=timezone.now().date() + timedelta(days=1),
        priority="medium",
        category=create_category,
        status="pending",
        created_by=create_user
    )
    task.assigned_users.set([create_user])
    assert task.title == "Sample Task"
    assert not task.is_overdue
    assert task.category.name == 'Development'


def test_due_date_cannot_be_past(db):
    with pytest.raises(ValidationError):
        task = Task(
            title="Past Task",
            description="Invalid",
            due_date=timezone.now().date() - timedelta(days=1),
            priority="low",
            status="pending"
        )
        task.full_clean()


def test_profile_created_on_user_creation(db):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    user = User.objects.create_user(username='user2', password='pass')
    assert hasattr(user, 'profile')
    assert user.profile is not None


def test_is_overdue_property(db, create_user, create_category):
    # Test a task that is overdue
    overdue_task = Task.objects.create(
        title="Overdue Task",
        description="This task is overdue.",
        due_date=timezone.now().date() - timedelta(days=1),
        priority="high",
        category=create_category,
        status="pending",
        created_by=create_user
    )
    assert overdue_task.is_overdue

    # Test a task that is not overdue (due date is in the future)
    future_task = Task.objects.create(
        title="Future Task",
        description="This task is not overdue.",
        due_date=timezone.now().date() + timedelta(days=1),
        priority="low",
        category=create_category,
        status="pending",
        created_by=create_user
    )
    assert not future_task.is_overdue

    # Test a task that is done, even if the due date is in the past
    done_task = Task.objects.create(
        title="Done Task",
        description="This task is done.",
        due_date=timezone.now().date() - timedelta(days=1),
        priority="low",
        category=create_category,
        status="done",
        created_by=create_user
    )
    assert not done_task.is_overdue
