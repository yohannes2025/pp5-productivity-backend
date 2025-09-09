from django.test import TestCase
from django.contrib.auth import get_user_model
from productivity_app.models import Task, Category, File

User = get_user_model()


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="password")
        self.category = Category.objects.create(name="Work")
        self.task = Task.objects.create(
            title="Test Task",
            description="Task description",
            owner=self.user,
            category=self.category,
            priority="High",
            state="Open"
        )

    def test_task_str(self):
        self.assertEqual(str(self.task), "Test Task")

    def test_task_owner(self):
        self.assertEqual(self.task.owner.username, "testuser")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Work")


class FileModelTest(TestCase):
    def test_file_str(self):
        file = File.objects.create(file="uploads/test.txt")
        self.assertIn("test.txt", str(file))
