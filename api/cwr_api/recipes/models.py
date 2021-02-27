from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

# Create your models here.

"""
Represents all blog posts. Initial entry into application filters based to the selected type.
"""
class Posts(models.Model):
    class PostTypes(models.TextChoices):
        RECIPE = 'R', _("Recipe")
        TECHNIQUE = 'T', _("Technique")
        EXPERIENCE = 'E', _("Experience") 
    post_type = models.CharField(max_length=1, choices=PostTypes.choices, default=PostTypes.RECIPE)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
    
    def posts_count(self, post_type=None, **kwargs):
        if post_type:
            return len(Posts.objects.filter(models.Q(post_type__contains=post_type)))
        return len(Posts.objects.all())
    

"""
Represents instructions to make food dishes. Accessed by selecting "Recipes" upon entry to application.
"""
class Recipes(models.Model):
    class MealTypes(models.TextChoices):
        SOUP_STEW = 'S', _("Soup/Stew")
        SALAD = 'SD', _("Salad")
        PASTA = 'P', _("Pasta")
        CHICKEN = 'CK', _("Chicken")
        BEEF = 'B', _("Beef")
        PORK = 'PK', _("Pork")
        VEGETABLE = 'V', _("Vegetable")
        FISH = 'F', _("Fish")
        BREAKFAST = 'BF', _("Breakfast")
        CONDIMENT = 'C', _("Condiment")
    post_key = models.ForeignKey(Posts, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=2, choices=MealTypes.choices, default=MealTypes.BREAKFAST)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    servings = models.SmallIntegerField()
    
    def recipes_count(self, meal_type=None, **kwargs):
        if meal_type:
            return len(Recipes.objects.filter(models.Q(meal_type__contains=meal_type)))
        return len(Recipes.objects.all())
    
"""
Represents items needed to complete recipes and their quantities.
"""
class Ingredients(models.Model):
    class UnitOfMeasurement(models.TextChoices):
        GRAM = 'G', _("Gram")
        OUNCE = 'O', _("Ounce")
        TABLESPOON = 'TBSP', _("Tablespoon")
        TEASPOON = 'TSP', _("Teaspoon")
        CUP = 'C', _("Cup")
        COUNT = 'CNT', _("Count")
        POUND = 'P', _("Pound")
    recipe_key = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=4, choices=UnitOfMeasurement.choices, default=UnitOfMeasurement.GRAM)
    
"""
Represents instructions/detailed steps for completing recipe
"""    
class Instructions(models.Model):
    recipe_key = models.ForeignKey(Posts, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    display_order = models.IntegerField()
    
    