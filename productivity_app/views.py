# productivity_app/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, ProfileSerializer, TaskSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .models import Profile, Task
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

User = get_user_model()


class RegisterViewSet(generics.CreateAPIView):
    """
    Handles user registration.
    """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """
        Handle POST request for user registration.
        Uses a transaction to ensure atomicity (user and profile creation).
        """
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # Call perform_create to create the user
            user = self.perform_create(serializer)

            refresh = RefreshToken.for_user(user)
            response_data = {
                'message': 'User registered successfully',
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        """
        Custom perform_create to return the created user instance.
        """
        return serializer.save()


class LoginViewSet(views.APIView):
    """
    Handles user login and token generation.
    """

    def post(self, request, *args, **kwargs):
        """
        Handle POST request for user login.
        """
        serializer = LoginSerializer(
            data=request.data, context={'request': request})

        serializer.is_valid(raise_exception=True)

        # If valid, the user is in validated_data
        user = serializer.validated_data['user']

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        # Return tokens in the response
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, status=status.HTTP_200_OK)


class UserDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['priority', 'category', 'status']
    search_fields = ['title', 'description']

    def perform_create(self, serializer):
        serializer.save()


class UsersListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
