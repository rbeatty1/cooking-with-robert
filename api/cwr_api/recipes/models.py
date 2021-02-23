from django.db import models
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
    

"""
Represents instructions to make food dishes. Accessed by selecting "Recipes" upon entry to application.
"""
class Recipes(models.Model):
    class MealTypes(models.TextChoices):
        BREAKFAST = 'BF', _("Breakfast")
        LUNCH = 'L', _("Lunch")
        DINNER = 'DN', _("Dinner")
        DESSERT = 'DS', _("Dessert")
        SNACK = 'S', _("Snack")
        CONDIMENT = 'C', _("Condiment")
    post_key = models.ForeignKey(Posts, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=2, choices=MealTypes.choices, default=MealTypes.BREAKFAST)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    servings = models.SmallIntegerField()
    
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
    
    