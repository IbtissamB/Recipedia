#The "GPS" that tells Django which View to run based on the URL.

from django.urls import path
from .views import RecipeList, RecipeDetail

urlpatterns = [
    # Path: /api/recipes/
    path('recipes/', RecipeList.as_view(), name='recipe-list'),
    
    # Path: /api/recipes/1/ (The <int:pk> captures the ID of the recipe)
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
]