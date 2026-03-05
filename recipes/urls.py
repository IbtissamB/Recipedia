#The "GPS" that tells Django which View to run based on the URL.

from django.urls import path
from .views import RecipeList, RecipeDetail, CategoryList, CategoryDetail, IngredientDetail, IngredientList

urlpatterns = [
    # Recipe Endpoints
    # Path: /api/recipes/
    path('recipes/', RecipeList.as_view(), name='recipe-list'),
    
    # Path: /api/recipes/1/ (The <int:pk> captures the ID of the recipe)
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),

    # Category Endpoints
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),

    # Ingredient Endpoints
    path('api/ingredients/', IngredientList.as_view(), name='ingredient-list'),
    path('api/ingredients/<int:pk>/', IngredientDetail.as_view(), name='ingredient-detail'),
]