#The "Brains" that handle the requests (GET, POST, etc.).

from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Recipe
from .serializers import RecipeSerializer

# ListCreateAPIView: Handles GET (list all) and POST (create new).
class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all() # Fetch all recipes from DB
    serializer_class = RecipeSerializer

    # 'IsAuthenticatedOrReadOnly' means: 
    # Anyone can SEE recipes, but you must LOGIN to create one.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # This function runs right before a new recipe is saved.
        # This automatically sets the 'author' to the logged-in user
        serializer.save(author=self.request.user)

# RetrieveUpdateDestroyAPIView: Handles GET (one item), PUT (edit), and DELETE.
class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
