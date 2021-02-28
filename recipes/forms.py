from django.forms import ModelForm

from recipes.models import Recipe, RecipeIngredient


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('author', 'name', 'image', 'description', 'tag', 'time')


class RecipeIngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ('recipe', 'ingredient', 'amount')
