import random
import string

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.text import slugify

from users.models import User


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        related_name='recipe'
    )
    name = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='recipe', blank=False)
    description = models.TextField(max_length=300, blank=False)
    tag = ArrayField(base_field=models.CharField(max_length=10, blank=False))
    time = models.IntegerField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        letters = string.ascii_lowercase

        while Recipe.objects.filter(slug=self.slug):
            self.slug += random.choice(letters)

        super().save(*args, **kwargs)


class Ingredient(models.Model):
    title = models.CharField(max_length=200, blank=False)
    dimension = models.CharField(max_length=10, blank=False)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        blank=False,
        related_name='recipe_ingredient'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        blank=False,
        related_name='recipe_ingredient'
    )
    amount = models.IntegerField()


class ShoppingList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_list'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_list'
    )

    class Meta:
        unique_together = ('user', 'recipe')


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        unique_together = ('user', 'author')

    def __str__(self):
        return f'{self.user} followed {self.author}'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favourite'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favourite'
    )
