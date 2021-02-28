from django.contrib import admin

from recipes.models import (Favorite, Follow, Ingredient, Recipe,
                            RecipeIngredient, ShoppingList)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_filter = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_filter = ('title',)


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_filter = ('amount',)


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_filter = ('user',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_filter = ('user',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_filter = ('user',)
