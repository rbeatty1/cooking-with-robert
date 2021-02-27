from django.test import TestCase
from .models import Posts, Recipes, Ingredients, Instructions

# Create your tests here.

#Posts tests
class PostsTest(TestCase):
    @classmethod
    def setUp(self):
        self.post_1 = Posts.objects.create(post_type=Posts.PostTypes.TECHNIQUE)
        self.post_2 = Posts.objects.create()
        return self
        
    def test_default_posts(self):
        """New posts with no post_type arg passed should create record with value 'R'"""
        self.assertEqual(self.post_2.post_type, Posts.PostTypes.RECIPE)
    
    def test_assigned_post_type(self):
        """New posts with post_type arg passed should create record with that value"""
        self.assertEqual(self.post_1.post_type, Posts.PostTypes.TECHNIQUE)
        
    def test_post_count_all(self):
        """Count should equal total post count"""
        self.assertEqual(Posts.posts_count(self), 2)
        
    def test_post_count_type(self):
        """Count should equal post count of passed type"""
        self.assertEqual(Posts.posts_count(self, post_type=Posts.PostTypes.TECHNIQUE), 1)

#Recipes tests
class RecipesTests(TestCase):
    @classmethod
    def setUp(self):
        self.post = Posts.objects.create()
        self.recipe_1 = Recipes.objects.create(post_key=self.post, meal_type=Recipes.MealTypes.BREAKFAST, name="Test Recipe (Breakfast) 1", description="Recipe 1 Unit Test", servings=1)
        self.recipe_2 = Recipes.objects.create(post_key=self.post, meal_type=Recipes.MealTypes.SOUP_STEW, name="Test Recipe 2", description="Recipe 2 Unit Test", servings=5)
        return self
        
    def test_assigned_post_type(self):
        """New posts with meal_type arg passed should create record with that value"""
        self.assertEqual(self.recipe_1.meal_type, Recipes.MealTypes.BREAKFAST)
        self.assertEqual(self.recipe_2.meal_type, Recipes.MealTypes.SOUP_STEW)
        
    def test_recipe_count_all(self):
        """Count should equal total recipe count"""
        self.assertEqual(Recipes.recipes_count(self), 2)
        
    def test_recipe_count_type(self):
        """Count should equal post count of passed type"""
        self.assertEqual(Recipes.recipes_count(self, meal_type=Recipes.MealTypes.BREAKFAST), 1)
        self.assertEqual(Recipes.recipes_count(self, meal_type=Recipes.MealTypes.SOUP_STEW), 1)
    
class IngredientsTests(TestCase):
    @classmethod
    def setUp(self):
        self.recipe = RecipesTests.setUp()
        self.ingred_1 = Ingredients.objects.create(recipe_key=self.recipe.recipe_1, name="Test Ingredient 1", quantity=4, unit=Ingredients.UnitOfMeasurement.GRAM)
        self.ingred_2 = Ingredients.objects.create(recipe_key=self.recipe.recipe_2, name="Test Ingredient 2", quantity=4, unit=Ingredients.UnitOfMeasurement.OUNCE)
    
    def test_ingredient_all(self):
        """Count should equal total ingredient count"""
        self.assertEqual(len(Ingredients.objects.all()), 2)
    
class InstructionsTests(TestCase):
    @classmethod
    def setUp(self):
        self.post = PostsTest.setUp()
        self.inst_1 = Instructions.objects.create(recipe_key=self.post.post_1, description="Test Instructions 1", display_order=1)
        self.inst_2 = Instructions.objects.create(recipe_key=self.post.post_2, description="Test Instructions 2", display_order=2)
    
    def test_instruction_all(self):
        """Count should equal total ingredient count"""
        self.assertEqual(len(Instructions.objects.all()), 2)
        