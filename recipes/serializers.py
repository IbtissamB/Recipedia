#Django REST Framework (DRF)
#Serializer is like translator. It takes yourthe complex Python Recipe object and 
# translates it into a simple JSON format.


from rest_framework import serializers
from .models import Recipe, Category, Ingredient

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

class RecipeSerializer(serializers.ModelSerializer):
    # These show the names of the category/author instead of just their ID numbers
    category_name = serializers.ReadOnlyField(source='category.name')
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Recipe

        # List every field you want to show in your API output
        fields = [
            'id', 'title', 'description', 'instructions', 
            'prep_time', 'cook_time', 'servings', 
            'created_at', 'author', 'author_username', 
            'category', 'category_name', 'ingredients'
        ]
        #'read_only_fields' means the USER cannot change these manually.
        #the 'author' is handled in the view, and 'id' is automatic.
        read_only_fields = ['author'] # The API will set the author automatically later