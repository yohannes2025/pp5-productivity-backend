# productivity_app/serializers.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import (
    LoginViewSet,
    TaskViewSet,
    ProfileViewSet,
    RegisterViewSet,
    UsersListAPIView,
    UserDetailAPIView,
)


app_name = "productivity_app"

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('api/register/', RegisterViewSet.as_view(), name='register'),
    path('api/login/', LoginViewSet.as_view(), name='login'),

    # JWT token endpoints (Simple JWT)
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),

    path('api/token/verify/', TokenVerifyView.as_view(),
         name='token_verify'),

    # viewsets
    path('api/', include(router.urls)),

    # User list and detail endpoints
    path('api/users/', UsersListAPIView.as_view(), name='users-list'),
    path('api/users/me/', UserDetailAPIView.as_view(), name='user-detail'),
]
