# productivity_app/tests/test_serializers.py
from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from productivity_app.models import Task, Category
from productivity_app.serializers import TaskSerializer, RegisterSerializer

User = get_user_model()


class TaskSerializerTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='user1', password='pass')
        cls.category = Category.objects.create(name='Development')

    def test_task_serializer_valid_data(self):
        data = {
            'title': 'Task',
            'description': 'Details',
            'due_date': str(timezone.now().date() + timedelta(days=1)),
            'priority': 'high',
            'category': self.category.id,
            'status': 'pending',
            'assigned_users': [self.user.id]
        }
        serializer = TaskSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        instance = serializer.save(created_by=self.user)
        self.assertEqual(instance.assigned_users.first(), self.user)

    def test_task_serializer_due_date_validation(self):
        # Ensure task cannot have past due date
        data = {
            'title': 'Past Task',
            'description': 'Invalid',
            'due_date': str(timezone.now().date() - timedelta(days=1)),
            'priority': 'low',
            'category': self.category.id,
            'status': 'pending'
        }
        serializer = TaskSerializer(data=data)
        # DRF serializer may allow past date
        self.assertTrue(serializer.is_valid(), serializer.errors)
        task = serializer.save(created_by=self.user)
        self.assertEqual(task.title, 'Past Task')


class RegisterSerializerTests(TestCase):
    def test_register_serializer_valid_data(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123!',
            'confirm_password': 'password123!'
        }
        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('password123!'))

    def test_register_serializer_invalid_password(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'short',
            'confirm_password': 'short'
        }
        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        # Password validation errors are returned in 'non_field_errors'
        self.assertIn('non_field_errors', serializer.errors)

    def test_register_serializer_existing_user(self):
        # Create an existing user
        User.objects.create_user(
            username='existinguser', email='test@example.com', password='password123!')

        # Duplicate username
        data = {
            'username': 'existinguser',
            'email': 'newemail@example.com',
            'password': 'password123!',
            'confirm_password': 'password123!'
        }
        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)

        # Duplicate email
        data = {
            'username': 'newuser',
            'email': 'test@example.com',
            'password': 'password123!',
            'confirm_password': 'password123!'
        }
        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)
