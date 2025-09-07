# productivity_app/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
    """
    Extends the built-in User model with additional profile information.
    Uses a OneToOneField to link each Profile to a User.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='profile'
    )
    created_at = models.DateTimeField(
        auto_now_add=True)  # Temporary default
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(
        max_length=254, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user}" if self.user else "Profile"


# Signal handler for creating Profile
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Connect the signal to the User model
post_save.connect(create_profile, sender=User)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    Represents a task that can be assigned to one or more users.
    Includes metadata like due date, priority, and optional file attachments.
    """
    # Choices for the 'status' field
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    # Choices for the 'category' field
    CATEGORY_CHOICES = [
        ('development', 'Development'),
        ('design', 'Design'),
        ('testing', 'Testing'),
        ('documentation', 'Documentation'),
        ('other', 'Other'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)  # optional due date
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    assigned_users = models.ManyToManyField(
        User, related_name='assigned_tasks'
    )
    created_by = models.ForeignKey(
        User,
        related_name='created_tasks',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['due_date', 'priority', 'status']

    def clean(self):
        # Validate that due_date is not in the past
        if self.due_date and self.due_date < timezone.now().date():
            raise ValidationError("Due date cannot be in the past.")

    def save(self, *args, **kwargs):
        self.clean()  # call clean before saving
        super().save(*args, **kwargs)

    @property
    def is_overdue(self):
        """Checks if the task's due date is in the past."""
        if self.due_date:
            return timezone.now().date() > self.due_date and self.status != 'done'
        return False

    def __str__(self):
        return self.title
