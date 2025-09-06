# productivity_app/urls.py

from django.urls import path, include
from .views import RegisterViewSet, LoginViewSet, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = 'productivity_app'

urlpatterns = [
    path('api/register/', RegisterViewSet.as_view(), name='register'),
    path('api/login/', LoginViewSet.as_view(), name='login'),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/users/me/', UserDetailView.as_view(), name='user-detail'),
]
