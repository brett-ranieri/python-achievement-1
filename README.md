### Table of Contents

[Exercise 1](https://github.com/brett-ranieri/python-achievement-1/tree/main#exercise-1)

[Exercise 2](https://github.com/brett-ranieri/python-achievement-1/tree/main#exercise-2)

[Exercise 3](https://github.com/brett-ranieri/python-achievement-1/tree/main#exercise-3)

[Exercise 4](https://github.com/brett-ranieri/python-achievement-1/tree/main#exercise-4)


## Exercise 1

#### Install Python

Install Python 3.8.7 and check for appropriate version by running `python --version`

#### Setup Virtual Environment

Run the following command to create a new virtual environment `mkvirtualenv cf-python-base`

#### Create Python Script

Open VsCode and create a file named add.py. In this file write simple code asking user to input two numbers, each assigned to their own variable. Once received have script add numbers together and return the answer as a third variable. Then print the solution.

#### Setup ipython Shell

Install ipython with the following command `pip install ipython` then test ipython shell bu running `ipython`

#### Export Requirements File

Use `pip freeze > requirements.txt` to create a requirements file. Then create a new environment named `cf-python-copy`. Finally, within the new environment run `pip install -r requirements.txt`


## Exercise 2

#### Create a template recipe structure

A dictionary makes the most sense for an individual recipe becuase of it's built in key:value structure that matches the requirements of the recipe. It will support manipulation and access to the recipe data which will be useful for future interactions.

#### Create Tea recipe following key:value prompts in exercise

`In [1]: recipe_1 = {
   ...: 'name': 'Tea',
   ...: 'cooking_time' : 5,
   ...: 'ingredients' : ['Tea leaves', 'Sugar', 'Water']
   ...: }`

#### Create an outer structure in which to store recipes

A list makes sense for this structue as it is an ordered sequence built into Python, fulfilling the first part of the brief. Lists are also mutable, allowing for all of their internal elements to be modified or deleted as needed, which is also specified in the brief. 

#### Create more recipes to fill all_recipes list 

Additional recipes are similar top structure for Tea recipe shown above. Add to all_recipes with append `all_recipes.append(recipe_2)`

#### Print ingredients of each recipe as their own list

Ingredients are built as a list within the structure, so just need to print for each recipe `print(all_recipes[0]['ingredients']`


## Exercise 3

#### Create file and initialize two empty lists

Use file > new in vscode and save file to appropriate folder. Initialize an empty list with `recipes_list = []`

#### Define a function called take_recipe

`def take_recipe():
    name = str(input("Enter recipe name: "))
    cooking_time = int(input("Enter total cooking time: "))
    ingredients = str(input("Enter ingredients, each seperated by a comma: ")).split(", ")
    ingredients = [i.title() for i in ingredients]
    recipe = {
      "name": name.capitalize(),
      "cooking_time": cooking_time,
      "ingredients": ingredients
    }
    return(recipe)`

#### Ask user how many receipes they want to add and store in variable

`n = int(input("How many recipes would you like to enter: "))`

#### Run a for loop 'n' times to take and store recipes/compare ingredients to list

`for i in range(0,n):
    recipe = take_recipe()
    for ele in recipe['ingredients']:
      if ele not in ingredients_list:
        ingredients_list.append(ele)
    recipes_list.append(recipe)`

#### Run a for loop to assign difficulties to recipes and display them

`for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
      recipe['difficulty'] = 'Easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
      recipe['difficulty'] = 'Medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
      recipe['difficulty'] = 'Intermediate'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
      recipe['difficulty'] = 'Hard' 
    else:
      recipe['difficulty'] = 'Unknown'
    print('')
    print('Recipe:', recipe['name'])
    print('Cooking Time (min):', recipe['cooking_time'])
    print('Ingredients:')
    for ele in recipe['ingredients']:
       print(ele)
    print('Difficulty level:', recipe['difficulty'])
    print('')`

#### Display ingredients list

`ingredients_list.sort()
print('-----------------------------------')
print('Ingredients Used Across All Recipes')
print('-----------------------------------')
for ele in ingredients_list:
  print('-', ele)`


## Exercise 4

### Part 1: recipe_input.py Script

#### Import Pickle

`import pickle`

#### Define a function called take_recipe()

Similar to exercise 1.3, but this time the difficulty is assigned in this function by calling calc_difficulty()

`def take_recipe():
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
    return recipe`

#### Define a function called calc_difficulty()

Exact same code as exercise 1.3

`def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    if cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    if cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    if cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "Hard"
    return difficulty`

#### Define a try-except-else-finally block

After the user provides a filename the try block attempts to open it. If it succeeds user is informed and code moves on to else

`filename = input("Enter filename where you've stored your recipes: ")`

`try:
    file = open(filename, "rb")
    data = pickle.load(file)
    print("File loaded successfully!")`

If FileNotFoundError user is informed and empty lists are created

`except FileNotFoundError:
    print("No files match that name - creating a new one")
    data = {"recipes_list": [], "all_ingredients": []}`

If other error, inform user then create new dictionary

`except:
    print("Oops, there was an unexpected error")
    data = {"recipes_list": [], "all_ingredients": []}`

else used to close file

`else:
    file.close()`

finally used to extract values from dictionary into two seperate lists

`finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]`


#### Ask user how many recipes they will enter, run for loop

Takes provided number and runs take_recipe() that number of times. Adding recipes and ingredients to perspective lists. 

`n = int(input("How many recipes would you like to enter: "))`

`for i in range(0, n):
    recipe = take_recipe()
    for ele in recipe["ingredients"]:
        if ele not in all_ingredients:
            all_ingredients.append(ele)
    recipes_list.append(recipe)
    print("Recipe added!")`

#### Gather updated lists and write data to binary file

Update the data dictionary, then using filename provided by users write the updated data to that file

`data = {"recipes_list": recipes_list, "all_ingredients": all_ingredients}`

`updated_file = open(filename, "wb")`

`pickle.dump(data, updated_file)`

`updated_file.close()
print("Recipe file has been updated.")`

### Part 2: recipe_search.py Script

#### Import Pickle

`import pickle`

#### Define a function called display_recipe()

Similar to exercise 1.3, writing function to display recipe information

`def display_recipe(recipe):
    print("")
    print("Recipe: ", recipe["name"])
    print("Cooking Time (mins): ", recipe["cooking_time"])
    print("Ingredients: ")
    for ele in recipe["ingredients"]:
        print("- ", ele)
    print("Difficulty: ", recipe["difficulty"])
    print("")`

#### Define a function called search_ingredients() 

Shows user all ingredients on list, while assigning a number to each ingredient

`def search_ingredients(data):
    lst = enumerate(data["all_ingredients"])
    numbered_lst = list(lst)
    print("Ingredients List: ")
    for ele in numbered_lst:
        print(ele[0], ele[1])`

try block where user gets to pick a number that matches ingredient, if successful, sets ingredient as `ingredient_searched`

`try:
        num = int(input("Enter number for ingredient you would like to search: "))
        ingredient_searched = numbered_lst[num][1]
        print("Searching for...", ingredient_searched, "...")`

except block for value error, tells user only intergers are accepted

`except ValueError:
        print("Only Intergers accepted")`

except block for all other errors

`except:
        print(
            "Oops, your input didn't match the allowed options. Make sure you choose a number that matches an ingredient on the list"
        )`

else block that checks recipes for matching ingredients, prints any recipe including `searched_ingredient`

`else:
        for ele in data["recipes_list"]:
            if ingredient_searched in ele["ingredients"]:
                print(ele)`

#### Ask user to provide filename

`filename = input("Enter filename where you've stored your recipes: ")`

#### try-excpet-else block to load file

try block to load provided filename

`try:
    file = open(filename, "rb")
    data = pickle.load(file)
    print("File loaded successfully!")`

except block for FileNotFoundError

`except FileNotFoundError:
    print("No files match that name - please try again")`

except block for all other errors

`except:
    print("Oops, there was an unexpected error")`

else block to close file and run `search_ingredients()`

`else:
    file.close()
    search_ingredients(data)`



