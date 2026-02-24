from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    # This view only allows POST requests to create a new user
    queryset = User.objects.all()
    
    # Allow anyone to access this! Otherwise, people couldn't sign up.
    permission_classes = [permissions.AllowAny]
    
    serializer_class = RegisterSerializer