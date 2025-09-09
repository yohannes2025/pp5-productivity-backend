from django.test import TestCase
from productivity_app.serializers import TaskSerializer
from productivity_app.models import Task, Category
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="password")
        self.category = Category.objects.create(name="Personal")
        self.task_data = {
            "title": "New Task",
            "description": "Some description",
            "owner": self.user.id,
            "category": self.category.id,
            "priority": "Medium",
            "state": "Open",
        }

    def test_valid_serializer(self):
        serializer = TaskSerializer(data=self.task_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer_missing_title(self):
        invalid_data = self.task_data.copy()
        invalid_data.pop("title")
        serializer = TaskSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
