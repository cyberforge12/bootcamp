class Recipe:
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, recipe_type: str, descr=None):
        if name:
            self.name = name
        else:
            raise ValueError('No recipe name')
        if cooking_lvl in range(1,6):
            self.cooking_lvl = cooking_lvl
        else:
            raise ValueError('Incorrect cooking level. Provide a number between 1 and 5')
        if (type(cooking_time) is int and cooking_time > 0):
            self.cooking_time = cooking_time
        else:
            raise ValueError('Incorrect cooking time. Provide a positive number')
        if ingredients[0]:
            self.ingredients = ingredients
        else:
            raise ValueError('Please provide a list of ingredients')
        self.description = descr
        if recipe_type in ['starter', 'lunch', 'dessert']:
            self.recipe_type = recipe_type
        else:
            raise ValueError('Please provide a correct recipe type: starter, lunch or dessert')

    def __str__(self):
        """Return the string to print with the recipe info"""
        name = "Recipe for:\t\t\t{}".format(self.name)
        cook_lvl = "Cooking level:\t\t{}".format(self.cooking_lvl)
        ingr_txt = "Ingredients list:\t{}".format(', '.join(self.ingredients))
        meal = "To be eaten for:\t{}".format(self.recipe_type)
        times = "Cooking time:\t\t{} minutes.".format(self.cooking_time)
        descr = "Description:\t\t{}".format(self.description)
        txt = '\n'.join([name, cook_lvl, ingr_txt, meal, times, descr]) + '\n'
        return txt

