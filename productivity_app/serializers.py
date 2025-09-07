# productivity_app/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import Profile, Task, File

User = get_user_model()


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
    """Serializer for user login using email."""
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError(
                'Email and password are required.', code='authorization')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'Invalid credentials.', code='authorization')

        if not user.check_password(password):
            raise serializers.ValidationError(
                'Invalid credentials.', code='authorization')

        if not user.is_active:
            raise serializers.ValidationError(
                'User account is disabled.', code='authorization')

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class FileSerializer(serializers.ModelSerializer):
    """Serializer for file uploads."""

    class Meta:
        model = File
        fields = ['id', 'file']


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile."""

    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def to_representation(self, instance):
        """Include user ID and fallback email from user if needed."""
        ret = super().to_representation(instance)
        if instance.user:
            ret['user_id'] = instance.user.id
            if not ret['email']:
                ret['email'] = instance.user.email
        return ret


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating Task."""
    assigned_users = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True,
        required=False
    )
    upload_files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'due_date', 'priority', 'category',
            'status', 'assigned_users', 'upload_files', 'created_at',
            'updated_at', 'is_overdue'
        ]
        read_only_fields = ['created_at', 'updated_at', 'is_overdue']

    def create(self, validated_data):
        assigned_users_data = validated_data.pop('assigned_users', [])
        task = Task.objects.create(**validated_data)
        task.assigned_users.set(assigned_users_data)
        return task

    def update(self, instance, validated_data):
        assigned_users_data = validated_data.pop('assigned_users', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if assigned_users_data is not None:
            instance.assigned_users.set(assigned_users_data)
        instance.save()
        return instance


class TaskListSerializer(serializers.ModelSerializer):
    """Serializer for listing tasks with summary info."""

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority',
                  'category', 'status', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class TaskDetailSerializer(serializers.ModelSerializer):
    """Serializer for detailed view of a task."""
    assigned_users = UserSerializer(many=True, read_only=True)
    assigned_user_ids = serializers.PrimaryKeyRelatedField(
        source='assigned_users',
        queryset=User.objects.all(),
        many=True,
        write_only=True,
    )
    upload_files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority',
                  'category', 'status', 'assigned_users', 'assigned_user_ids',
                  'upload_files', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
