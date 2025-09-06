# productivity_app/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=254, unique=True, blank=True)

    def __str__(self):
        return self.name or self.user.username


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance, name=instance.username, email=instance.email)


post_save.connect(create_profile, sender=User)
