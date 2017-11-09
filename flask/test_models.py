import unittest
from models.user import User
from models.categories import Category
from models.recipes import Recipe

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("matsiko", "dorynnamara@gmail.com", "password")

    def test_created_user(self):
        self.assertIsInstance(self.user, User, 'User not created')

    def test_add_recipe_category_category_added(self):
        self.assertEqual(self.user.add_recipe_category("dinner"),
                        "recipe category is added succesfully")

    def test_add_recipe_category_name_already_exists(self):
        self.user.add_recipe_category("dinner")
        self.assertEqual(self.user.add_recipe_category
                         ("dinner"),
                         "recipe category already exists")


    def test_edit_recipe_category_not_found(self):
        self.assertEqual(self.user.edit_recipe_category("absent", "newtype"),
                         "recipe_category not found")

    def test_edit_recipe_category_successful(self):
        self.user.add_recipe_category("Snacks")
        self.assertEqual(self.user.edit_recipe_category("Snacks","local foods"),"recipe_category not found")

    def test_delete_recipe_category_not_found(self):
        self.assertEqual(self.user.delete_recipe_category("not exist"), "recipe_category not found")

    def test_delete_recipe_category_deleted(self):
        self.user.add_recipe_category("lunch recipes")
        self.assertEqual(self.user.delete_recipe_category("lunch recipes"),
                         "recipe_category deleted")


class Recipe_categoryTest(unittest.TestCase):

    def setUp(self):
        self.title = Category("lunch")

    def test_recipe_instantiation(self):
        self.assertIsInstance(self.title,Category,
                              "Failed to instantiate")

    def test_add_recipe_added(self):
            self.assertEqual(self.title.add_recipe("pillawo"), "recipe added succesfully")

    def test_add_recipe_exists(self):
        self.title.add_recipe("pizza")
        self.assertEqual(self.title.add_recipe(
            "pizza"), "recipe already exists")

    def test_edit_recipe_not_found(self):
        self.assertEqual(self.title.edit_recipe(
            "chicken recipe", "beef recipe"), "no recipe to edit")


    def test_edit_recipe_edited_succesfully(self):
         self.title.add_recipe("pizza")
         self.assertEqual(self.title.edit_recipe("pizza", "chicken"), "recipe edited successfully")

    def test_delete_recipe_not_found(self):
          self.assertEqual(self.title.delete_recipe(
            "katogo"), "No recipe to delete")

    def test_recipe_item(self):
        self.title.add_recipe("katogo")
        self.assertEqual(self.title.delete_recipe("katogo"), "recipe deleted")


