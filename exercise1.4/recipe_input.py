import pickle


def take_recipe():
    name = str(input("Enter the recipe name: "))
    cooking_time = int(input("Enter the cooking time: "))
    ingredients = str(input("Enter ingredients, each seperated by a comma: ")).split(
        ", "
    )
    ingredients = [i.title() for i in ingredients]

    difficulty = calc_difficulty(cooking_time, ingredients)

    recipe = {
        "name": name.capitalize(),
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty,
    }
    return recipe


def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    if cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    if cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    if cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "Hard"
    return difficulty


# user provides filename
filename = input("Enter filename where you've stored your recipes: ")
# open file and load with pickle
try:
    file = open(filename, "rb")
    data = pickle.load(file)
    print("File loaded successfully!")
# if file not found inform user, then create new dictionary
except FileNotFoundError:
    print("No files match that name - creating a new one")
    data = {"recipes_list": [], "all_ingredients": []}
# if unexpected error inform user, then create new dictionary
except:
    print("Oops, there was an unexpected error")
    data = {"recipes_list": [], "all_ingredients": []}
else:
    file.close()
# extract values from dictionary into two seperate lists
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]

# user provides number of recipes
n = int(input("How many recipes would you like to enter: "))
# for loop runs 'n' times
for i in range(0, n):
    recipe = take_recipe()
    # checks for ingredient in ingredient list, if not there then adds it
    for ele in recipe["ingredients"]:
        if ele not in all_ingredients:
            all_ingredients.append(ele)
    # adds recipe to recipe list
    recipes_list.append(recipe)
    print("Recipe added!")

# update data dictionary with newly added recipes/ingredients
data = {"recipes_list": recipes_list, "all_ingredients": all_ingredients}

# re-open user specified file
updated_file = open(filename, "wb")
# update file with new data
pickle.dump(data, updated_file)
# close file
updated_file.close()
print("Recipe file has been updated.")
