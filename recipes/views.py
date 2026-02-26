#The "Brains" that handle the requests (GET, POST, etc.).

from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Recipe
from .serializers import RecipeSerializer
# Import the custom permission
from .permissions import IsAuthorOrReadOnly
# Add CategoryList and CategoryDetail to your imports
from .models import Recipe, Category, Ingredient
from .serializers import RecipeSerializer, CategorySerializer, IngredientSerializer

# ListCreateAPIView: Handles GET (list all) and POST (create new).
class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all() # Fetch all recipes from DB
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # 'IsAuthenticatedOrReadOnly' means Anyone can SEE recipes, but you must LOGIN to create one.

    # These power the Search and Filter features for the LIST
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'ingredients']
    search_fields = ['title', 'ingredients__name']
    ordering_fields = ['prep_time', 'cook_time', 'servings']

    def perform_create(self, serializer):
        # This function runs right before a new recipe is saved.
        # This automatically sets the 'author' to the logged-in user
        serializer.save(author=self.request.user)

# VIEW 2: Retrieve, Update, Delete a single recipe by ID
#We don't need 'filter_backends' here. Because we are already looking at ONE specific recipe (by ID).
class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

class CategoryList(generics.ListCreateAPIView):
    """
    Allows users to see all available categories (GET) 
    and admins to create new ones (POST).
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    # Anyone can see the list, but only logged-in users (or admins) 
    # should be able to create categories.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Allows users to see a single category by ID.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]