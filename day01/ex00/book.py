import time
from recipe import Recipe

class Book:
    def __init__(self, name: str):
        if name:
            self.name = name
        else:
            raise ValueError('No book name')
        self.last_update = time.localtime()
        self.creation_date = time.localtime()
        self.recipes_list = []

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        recipe = [i for i in self.recipes_list if i.name == name]
        if recipe:
            print(recipe[0])
        else:
            print("No recipe for {} in {}".format(name, self.name))

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        recipes = [i.name for i in self.recipes_list if i.recipe_type == recipe_type]
        if recipes:
            print("Recipes for {} in the {}:".format(recipe_type, self.name))
            for i in recipes:
                print('\t', i)
        else:
            print("No recipes for {} in {}".format(recipe_type, self.name))

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list.append(recipe)
        self.last_update = time.localtime()
        print("The recipe for", recipe.name, "was added to the", self.name)

    def __str__(self):
        """Return the book info"""
        name = "Book name:\t\t\t{}".format(self.name)
        creat = "Created on:\t\t\t{}".format(time.strftime("%Y-%m-%d %H:%M:%S", self.creation_date))
        last_up = "Last updated on:\t{}".format(time.strftime("%Y-%m-%d %H:%M:%S", self.last_update))
        recipes = "Number of recipes:\t{}".format(str(len(self.recipes_list)))
        txt = '\n'.join([name, creat, last_up, recipes])
        return txt
