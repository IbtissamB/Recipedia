from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(generics.CreateAPIView):
    # This view only allows POST requests to create a new user
    queryset = User.objects.all()
    
    # Allow anyone to access this! Otherwise, people couldn't sign up.
    permission_classes = [permissions.AllowAny]
    
    serializer_class = RegisterSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # You might want to restrict this so only admins can see all users
    permission_classes = [permissions.IsAdminUser]

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer