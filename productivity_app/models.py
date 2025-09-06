# productivity_app/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=254, unique=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.name or self.user.username


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance, name=instance.username, email=instance.email)


post_save.connect(create_profile, sender=User)


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    CATEGORY_CHOICES = [
        ('development', 'Development'),
        ('design', 'Design'),
        ('testing', 'Testing'),
        ('documentation', 'Documentation'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    category = models.CharField(
        max_length=100, choices=CATEGORY_CHOICES, blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending')
    assigned_users = models.ManyToManyField(
        User, related_name='assigned_tasks', blank=True)

    def clean(self):
        if self.due_date and self.due_date < timezone.now().date():
            raise ValidationError("Due date cannot be in the past.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    @property
    def is_overdue(self):
        if self.due_date and self.due_date < timezone.now().date() and self.status != 'done':
            return True
        return False

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
