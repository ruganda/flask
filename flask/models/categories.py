class Category:

    def __init__(self,title):
        self.title =title
        self.recipes = []

    def add_recipe(self, title):
        if title not in self.recipes:
            self.recipes.append(title)
            return "recipe added succesfully"
        return "recipe already exists"

    def edit_recipe(self,title,new_title):
        if title in self.recipes:
            self.recipes= [new_title for title in self.recipes]
            return "recipe edited successfully"
        return "no recipe to edit"

    def delete_recipe(self,title):
        if title in self.recipes:
            self.recipes.remove(title)
            return "recipe deleted"
        return "No recipe to delete"


