# drf_api/urls.py (updated)
from django.contrib import admin
from django.urls import path, include
from productivity_app.views import RegisterViewSet, LoginViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterViewSet.as_view(), name='register'),
    path('api/login/', LoginViewSet.as_view(), name='login'),
]
