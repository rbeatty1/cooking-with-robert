import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q
from .models import Posts, Recipes, Ingredients, Instructions

class PostType(DjangoObjectType):
    class Meta:
        model = Posts
class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipes
class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredients
class InstructionType(DjangoObjectType):
    class Meta:
        model = Instructions
        
        
class Query(graphene.ObjectType):
    posts = graphene.List(PostType, search=graphene.String())
    recipes = graphene.List(RecipeType, search=graphene.String())
    ingredients = graphene.List(IngredientType)
    instructions = graphene.List(InstructionType)
    
    def resolve_posts(self, info, search=None, **kwargs):
        # If search parameter exists, filter the posts to passed arg
        if search:
            filter_criteria = (
                Q(id__contains=search) | Q(post_type__contains=search)
            )
            return Posts.objects.filter(filter_criteria)
        return Posts.objects.all()
    
    def resolve_recipes(self, info, search=None, **kwargs):
        # If search parameter exists, filter the posts to passed arg
        if search:
            filter_criteria = (
                Q(id__contains=search) | Q(meal_type__contains=search)
            )
            return Recipes.objects.filter(filter_criteria)
        return Recipes.objects.all()
    
    def resolve_ingredients(self, info, **kwargs):
        return Ingredients.objects.all()
    
    def resolve_instructions(self, info, **kwargs):
        return Instructions.objects.all()