from book import Book
from recipe import Recipe

cake = Recipe('cake', 5, 60, ['floor', 'sugar', 'eggs'], 'dessert')
print(cake)
sandwich = Recipe('sandwich', 1, 10, ['bread', 'ham', 'salad'], 'lunch')
salad = Recipe('salad', 1, 10, ['salad', 'mayo', 'tomatoes'], 'lunch')
print(sandwich)
book = Book('Cookbook')
print(str(book))
book.add_recipe(cake)
book.add_recipe(sandwich)
book.add_recipe(salad)
print(str(book))

book.get_recipe_by_name('cake')
book.get_recipe_by_name('wrong_cake')
book.get_recipes_by_types('lunch')
book.get_recipes_by_types('wrong_lunch')
