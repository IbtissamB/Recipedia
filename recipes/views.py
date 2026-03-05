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

    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]

    # ---Search Feature ---
    # These allow users to use the ?search= keyword
    # added 'category__name' so we can search "Dessert" as a word.
    search_fields = ['title', 'category__name', 'ingredients__name', 'prep_time']

    ordering_fields = ['prep_time', 'cook_time', 'servings', 'created_at']

    # --- Optional Filters ---
    # These allow users to refine results (e.g., ?servings=4&cook_time=20)
    filterset_fields = {
        # This allows: ?category__name=Dessert
        'category__name': ['icontains', 'exact'], 
        # This allows: ?ingredients__name=chicken
        'ingredients__name': ['icontains', 'exact'],
        # These allow: ?prep_time__lte=30
        'prep_time': ['exact', 'lte', 'gte'],
        'cook_time': ['exact', 'lte', 'gte'],
        'servings': ['exact'],
    }

    # This function runs right before a new recipe is saved.
    # This automatically sets the 'author' to the logged-in user
    def perform_create(self, serializer):
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

#Allows users to see a single category by ID.
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# VIEW: List all ingredients (GET) or Create a new one (POST)
class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    # Allow anyone to see, but must be logged in to add a new ingredient
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# VIEW: Get, Update, or Delete a specific ingredient by ID
class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]