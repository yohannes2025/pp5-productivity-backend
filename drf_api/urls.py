# drf_api/urls.py (updated)
from django.contrib import admin
from django.urls import path, include
from productivity_app.views import RegisterViewSet, LoginViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from productivity_app.views import UserDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterViewSet.as_view(), name='register'),
    path('api/login/', LoginViewSet.as_view(), name='login'),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/users/me/', UserDetailView.as_view(), name='user-detail'),
]
