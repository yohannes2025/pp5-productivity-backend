# productivity_app/tests/test_urls.py
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from productivity_app.views import (
    LoginViewSet,
    TaskViewSet,
    ProfileViewSet,
    RegisterViewSet,
    UsersListAPIView,
    UserDetailAPIView,
)


class TestUrls(SimpleTestCase):

    def test_register_url_resolves(self):
        url = reverse("productivity_app:register")
        self.assertEqual(resolve(url).func.view_class, RegisterViewSet)

    def test_login_url_resolves(self):
        url = reverse("productivity_app:login")
        self.assertEqual(resolve(url).func.view_class, LoginViewSet)

    def test_token_obtain_pair_url_resolves(self):
        url = reverse("productivity_app:token_obtain_pair")
        self.assertEqual(resolve(url).func.view_class, TokenObtainPairView)

    def test_token_refresh_url_resolves(self):
        url = reverse("productivity_app:token_refresh")
        self.assertEqual(resolve(url).func.view_class, TokenRefreshView)

    def test_token_verify_url_resolves(self):
        url = reverse("productivity_app:token_verify")
        self.assertEqual(resolve(url).func.view_class, TokenVerifyView)

    def test_users_list_url_resolves(self):
        url = reverse("productivity_app:users-list")
        self.assertEqual(resolve(url).func.view_class, UsersListAPIView)

    def test_user_detail_url_resolves(self):
        url = reverse("productivity_app:user-detail")
        self.assertEqual(resolve(url).func.view_class, UserDetailAPIView)

    def test_task_viewset_list_url_resolves(self):
        url = reverse("productivity_app:task-list")
        self.assertEqual(resolve(url).func.cls, TaskViewSet)

    def test_profile_viewset_list_url_resolves(self):
        url = reverse("productivity_app:profile-list")
        self.assertEqual(resolve(url).func.cls, ProfileViewSet)
