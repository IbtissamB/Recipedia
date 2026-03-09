from django.contrib.auth.models import User
from rest_framework import serializers

# Use this ONLY for the register endpoint (POST)
class RegisterSerializer(serializers.ModelSerializer):
    # We want the password to be 'write_only' so it never shows 
    # up in the API response after the user is created.
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        """
        This function overrides the default 'create' method.
        We use 'create_user' because it automatically handles 
        password hashing (scrambling) for security.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user
    
# Use this for seeing all users (GET)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')