# productivity_app/auth/backends.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomAuthBackend(ModelBackend):
    """
    A custom authentication backend that allows users to log in with email.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
