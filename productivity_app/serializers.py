# productivity_app/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import Profile, Task

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    confirm_password = serializers.CharField(write_only=True)
    name = serializers.CharField(label='Name', required=True)
    email = serializers.EmailField(label='Email', required=True)

    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                {"password": "Passwords must match."})
        self.validate_password_strength(attrs['password'])

        if User.objects.filter(username=attrs['name']).exists():
            raise serializers.ValidationError({
                "name": "A user with this username already exists."
            })

        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({
                "email": "A user with this email already exists."
            })

        return attrs

    def validate_password_strength(self, password):
        try:
            validate_password(password)
        except serializers.ValidationError as e:
            raise serializers.ValidationError({'password': e.messages})

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        name = validated_data.pop('name')
        email = validated_data['email']
        password = validated_data['password']

        user = User.objects.create_user(
            username=name,
            email=email,
            password=password
        )

        try:
            profile = user.profile
            profile.name = name
            profile.save()
        except Profile.DoesNotExist:
            Profile.objects.create(user=user, name=name, email=email)

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError(
                'Email and password are required.')

        user = User.objects.filter(email=email).first()
        if user is None or not user.check_password(password):
            raise serializers.ValidationError('Invalid credentials.')

        if not user.is_active:
            raise serializers.ValidationError('User account is disabled.')

        attrs['user'] = user
        return attrs


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'avatar')


class TaskSerializer(serializers.ModelSerializer):
    assigned_users = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, required=False)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date',
                  'priority', 'category', 'status', 'assigned_users', 'is_overdue']
        read_only_fields = ['is_overdue']

    assigned_users = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, required=False)


def create(self, validated_data):
    assigned_users = validated_data.pop('assigned_users', [])
    task = super().create(validated_data)
    task.assigned_users.set(assigned_users)
    return task


def update(self, instance, validated_data):
    assigned_users = validated_data.pop('assigned_users', None)
    instance = super().update(instance, validated_data)
    if assigned_users is not None:
        instance.assigned_users.set(assigned_users)
    return instance
