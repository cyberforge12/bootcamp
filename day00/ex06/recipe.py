def print_recipe(name):
    try:
        cookbook[name]
        print("Recipe for {}:".format(name))
        print("Ingredients list:", list(cookbook[name]['ingredients']))
        print("To be eaten for", cookbook[name]['meal'])
        print("Takes", cookbook[name]['prep_time'], "minutes of cooking.")
    except Exception:
        print("No such recipe. Exiting to main menu")


def print_cookbook():
    print("Cookbook recipes:")
    for a in cookbook.keys():
        print("\t", a)
    print("")


def delete_recipe(name):
    del cookbook[name]
    print("The recipe for", name, "was deleted from the cookbook")


def add_recipe(name, ingredients, meal_type, p_time):
    cookbook[name] = {'ingredients': ingredients, 'meal': meal_type, 'prep_time': p_time}


cookbook = {}
add_recipe('sandwich', ['ham', 'bread', 'cheese', 'tomatoes'], 'lunch', 10)
add_recipe('cake', ['flour', 'sugar', 'eggs'], 'dessert', 60)
add_recipe('salad', ['avocado', 'arugula', 'tomatoes', 'spinach'], 'lunch', 15)
option = 0
while 1:
    if option not in [-1, 5]:
        print("Please select an option by typing the corresponding number:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
    option = input()
    if option == '5':
        print("Cookbook closed.")
        exit(0)
    elif option == '1':
        while 1:
            print("Please enter the recipe's name to add or [5] to leave to main menu:")
            while 1:
                recipe_name = input()
                try:
                    cookbook[recipe_name]
                    print("Such a recipe already exists. Choose another name or [5] for main menu:")
                except Exception:
                    break
            if recipe_name in ["5", None]:
                break
            else:
                print("Please enter the recipe's ingredients:")
                ingrs = list()
                while 1:
                    ingr = input()
                    if ingr == "":
                        break
                    else:
                        ingrs.append(ingr)
                print("Please enter the recipe's meal type:")
                meal = input()
                print("Please enter the recipe's cooking time in minutes:")
                prep_time = input()
                add_recipe(recipe_name, ingrs, meal, prep_time)
                break
    elif option == '2':
        print("Please enter the recipe's name to DELETE:")
        recipe_name = input()
        try:
            cookbook[recipe_name]
            delete_recipe(recipe_name)
        except Exception:
            print_recipe("No such recipe. Exiting to main menu")
    elif option == '3':
        print("Please enter the recipe's name to get its details:")
        recipe_name = input()
        print_recipe(recipe_name)
    elif option == '4':
        print_cookbook()
    else:
        option = -1
        print("This option does not exist, please type the corresponding number.")
        print("To exit, enter 5.")
