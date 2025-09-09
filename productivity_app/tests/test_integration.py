from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                {"password": "Passwords must match."})

        # Exclude confirm_password before validating password
        user_data = {k: v for k, v in attrs.items() if k != 'confirm_password'}
        try:
            validate_password(attrs['password'], user=User(**user_data))
        except serializers.ValidationError as e:
            raise serializers.ValidationError({'password': e.messages})

        # Check for existing email
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(
                {"email": "A user with this email already exists."})

        # Check for existing username
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError(
                {"username": "A user with this username already exists."})

        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
