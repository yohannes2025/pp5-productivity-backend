from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.contrib.auth import get_user_model

from productivity_app.models import Task, Profile, Category

User = get_user_model()


class TaskModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a sample user and category for all tests
        cls.user = User.objects.create_user(username='user1', password='pass')
        cls.category = Category.objects.create(name='Development')

    def test_task_creation(self):
        task = Task.objects.create(
            title="Sample Task",
            description="Test description",
            due_date=timezone.now().date() + timedelta(days=1),
            priority="medium",
            category=self.category,
            status="pending",
            created_by=self.user
        )
        task.assigned_users.set([self.user])

        self.assertEqual(task.title, "Sample Task")
        self.assertFalse(task.is_overdue)
        self.assertEqual(task.category.name, 'Development')

    def test_due_date_cannot_be_past(self):
        task = Task(
            title="Past Task",
            description="Invalid",
            due_date=timezone.now().date() - timedelta(days=1),
            priority="low",
            status="pending",
            created_by=self.user
        )
        with self.assertRaises(ValidationError):
            task.full_clean()

    def test_profile_created_on_user_creation(self):
        new_user = User.objects.create_user(username='user2', password='pass')
        self.assertTrue(hasattr(new_user, 'profile'))
        self.assertIsNotNone(new_user.profile)

    def test_is_overdue_property(self):
        # Task overdue
        overdue_task = Task.objects.create(
            title="Overdue Task",
            description="This task is overdue.",
            due_date=timezone.now().date() - timedelta(days=1),
            priority="high",
            category=self.category,
            status="pending",
            created_by=self.user
        )
        self.assertTrue(overdue_task.is_overdue)

        # Task not overdue
        future_task = Task.objects.create(
            title="Future Task",
            description="This task is not overdue.",
            due_date=timezone.now().date() + timedelta(days=1),
            priority="low",
            category=self.category,
            status="pending",
            created_by=self.user
        )
        self.assertFalse(future_task.is_overdue)

        # Task done, even if past due date
        done_task = Task.objects.create(
            title="Done Task",
            description="This task is done.",
            due_date=timezone.now().date() - timedelta(days=1),
            priority="low",
            category=self.category,
            status="done",
            created_by=self.user
        )
        self.assertFalse(done_task.is_overdue)
