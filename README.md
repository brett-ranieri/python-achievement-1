### Table of Contents

[Exercise 1](https://github.com/brett-ranieri/python-achievement-1/tree/main#exercise-1)

[Exercise 2](https://github.com/brett-ranieri/python-achievement-1/tree/main#exercise-2)

[Exercise 3](https://github.com/brett-ranieri/python-achievement-1/tree/main#exercise-3)

[Exercise 4](https://github.com/brett-ranieri/python-achievement-1/tree/main#exercise-4)

[Exercise 5](https://github.com/brett-ranieri/python-achievement-1/tree/main#exercise-5)

[Exercise 6](https://github.com/brett-ranieri/python-achievement-1/tree/main#exercise-6)


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


## Exercise 5

#### Define Recipe class

`class Recipe(object):`
  
  `def __init__(self, name):
    self.name = name
    self.ingredients = []
    self.cooking_time = 0
    self.difficulty = "Need cooking time and ingredients to determine difficulty"`

#### Define procedural methods

`def get_name(self):
    output = "Recipe Name: " + str(self.name)
    return output`
  
  `def get_cooking_time(self):
    output = "Cooking Time: " + str(self.cooking_time)
    return output`
  
  `def set_name(self):
    self.name = str(input("Enter Recipe name: "))`

  `def set_cooking_time(self, cooking_time):
    self.cooking_time = int(cooking_time)
    Recipe.calculate_difficulty(self)`

  `def add_ingredients(self, *ingredients):
    for ingredient in ingredients:
      if ingredient not in self.ingredients:
        self.ingredients.append(ingredient)
    Recipe.update_all_ingredients(self)
    Recipe.calculate_difficulty(self)`

  `def get_ingredients(self):
    output = "\nList of Ingredients: \n"
    for ingredient in self.ingredients:
      output += " - " + ingredient + "\n"
    return output`
  
  `def calculate_difficulty(self):
    if self.cooking_time < 10 and self.cooking_time > 0 and len(self.ingredients) < 4 and len(self.ingredients) > 0:
      self.difficulty = "Easy"
    if self.cooking_time < 10 and len(self.ingredients) >= 4:
      self.difficulty = "Medium"
    if self.cooking_time >= 10 and len(self.ingredients) < 4:
      self.difficulty = "Intermediate"
    if self.cooking_time >= 10 and len(self.ingredients) >= 4:
      self.difficulty = "Hard"`

  `def get_difficulty(self):
    if self.difficulty == None:
      difficulty = Recipe.calculate_difficulty(self)
      output = "Recipe difficulty: " + str(difficulty)
      return output
    else:
      output = "Recipe difficulty: " + str(self.difficulty)
      return output`
    
  `def search_ingredient(self, ingredient):
    return ingredient in self.ingredients`
  
  `def update_all_ingredients(self):
    for ingredient in self.ingredients:
      if ingredient not in Recipe.all_ingredients:
        Recipe.all_ingredients.append(ingredient)`

  `def __str__(self):
    output = "\nRecipe Name: " + str(self.name) + "\nCooking Time: " + str(self.cooking_time) + " minutes" + "\nDifficulty: " + str(self.difficulty) + "\nIngredients: \n"
    for ingredient in self.ingredients:
      output += " - " + ingredient + "\n"
    return output`

#### Define recipe_search function

`def recipe_search(data, search_term):
  print("Searching...")
  for recipe in data:
    if recipe.search_ingredient(search_term):
      print(recipe)`

#### Upload recipes

`tea = Recipe("Tea")
tea.set_cooking_time(5)
tea.add_ingredients("Tea", "Leaves", "Sugar", "Water")
print(tea)`

`coffee = Recipe("Coffee")
coffee.set_cooking_time(5)
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
print(coffee)`

`cake = Recipe("Cake")
cake.set_cooking_time(50)
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
print(cake)`

`banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.set_cooking_time(5)
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
print(banana_smoothie)`

#### Wrap recipes in list

`recipes_list = [tea, coffee, cake, banana_smoothie]`

#### Search recipes for specific ingredients

`print()
print("Search test 1: Water")
recipe_search(recipes_list, "Water")`

`print()
print("Search test 2: Sugar")
recipe_search(recipes_list, "Sugar")`

`print()
print("Search test 3: Bananas")
recipe_search(recipes_list, "Bananas")`

## Exercise 6

#### Create & Connect Database

`import mysql.connector`

`conn = mysql.connector.connect(
    host="localhost", user="python-two", passwd="AnotherPassword"
)`

`cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")
cursor.execute(
    """CREATE TABLE IF NOT EXISTS recipes(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  ingredients VARCHAR(255),
  cooking_time INT,
  difficulty VARCHAR(20)      
)"""
)`

#### Create Main Menu

`def main_menu(conn, cursor):
    # loop running main menu, continues until user chooses to quit
    choice = ""
    while choice != "quit":
        print("\n------------------------------------------------------")
        print("\nWhat would you like to do? Select from options below:")
        print("\n   1 - Create a Recipe")
        print("\n   2 - Search for a Recipe")
        print("\n   3 - Update a Recipe")
        print("\n   4 - Delete a Recipe")
        print("\nType 'quit' to exit the program")
        print("\n------------------------------------------------------")
        choice = input("\nEnter number of choice: ")
        print()`

        `if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "quit":
            quit_app(conn, cursor)`


`main_menu(conn, cursor)`

#### Create Recipe with create_recipe() function

`def create_recipe(conn, cursor):
    # request recipe name
    name = str(input("Enter the recipe name: "))
    # request cooking time
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = []
    # request ingredient one at a time
    ingredient = input(
        "Write an ingredient and press enter, type 'done' when finished: "
    )
    while ingredient != "done":
        # add ingredient to list
        ingredients.append(ingredient.title())
        # request additional ingredients
        ingredient = input("Enter another ingredient, or type 'done' to finish: ")
    # convert list into comma seperated string
    # necessary because MySQL does not support arrays
    ingredients = ", ".join(ingredients)`

    `difficulty = calc_difficulty(cooking_time, ingredients)`

   `cursor.execute(
        "INSERT INTO recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)",
        # specifying values to be added to database
        (name, ingredients, cooking_time, difficulty),
    )
    # commit recipe to database
    conn.commit()
    print()
    print("Recipe has been added!")`

`# moved outside of create recipe so it can be accessed by update recipe
def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    if cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    if cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    if cooking_time >= 10 and len(ingredients) >= 4:
        return "Hard"`

#### Search for Recipe with search_recipe()

`def search_recipe(conn, cursor):
    all_ingredients = []
    # select ingredients column
    cursor.execute("SELECT ingredients FROM recipes")
    # fetch select, NECESSARY to be able to access data
    results = cursor.fetchall()
    # nested for loop to access ingredients
    for row in results:
        for ingredient in row:
            # split each ingredient into substrings
            ingredients_list = ingredient.split(", ")
            # prevent duplicates in all_ingredients
            for i in ingredients_list:
                if i not in all_ingredients:
                    all_ingredients.append(i)
    # add number to each element of list
    lst = enumerate(all_ingredients)
    # structure enumerated data back into a list
    numbered_lst = list(lst)
    print()
    print("Full Ingredient List: ")
    print()
    # print number/ingredient
    for item in numbered_lst:
        print("   ", item[0], "-", item[1])
    print()
    try:
        # request user provide number for ingredient to search
        num = int(input("Enter number for ingredient you would like to search: "))
        print()
        # store searched ingredient in variable
        ingredient_searched = numbered_lst[num][1]
        print("Searching for...", ingredient_searched, "...")
    # handle non-interger inputs
    except ValueError:
        print()
        print("*Only Intergers accepted")
    # handle entry that doesn't match list item
    except:
        print()
        print(
            "*Oops, nothing matches that value. Make sure to pick a number that matches an ingredient"
        )
    else:
        # query to database for matching recipes
        cursor.execute(
            # first required parameter is sql query
            "SELECT name, cooking_time, difficulty, ingredients FROM recipes WHERE ingredients like %s",
            # MUST add "," at end...cursor.execute REQUIRES a tuple (or list, or dict) as second parameter
            (f"%{ingredient_searched}%",),
        )
        # fetch results
        returned = cursor.fetchall()
        # print info for each matching recipe
        for row in returned:
            print()
            print("Name:", row[0])
            print("Cooking Time:", row[1], "minutes")
            print("Difficulty:", row[2])
            print("Ingredients:", row[3])`

#### Update Recipe with update_recipe()

`def update_recipe(conn, cursor):
    cursor.execute("SELECT id, name FROM recipes")`

   `results = cursor.fetchall()`

    `for row in results:
        print("   ", row[0], "-", row[1])
        print()
    # put try else in while loop to isolate and prevent from impacting code flow
    while True:
        try:
            num = int(input("Enter the number for recipe to update: "))
        # handle non-interger inputs
        except ValueError:
            print()
            print("*Only Intergers accepted")
        else:
            break
    while True:
        try:
            options = (
                ("1 -", "Change Name"),
                ("2 -", "Change Cooking Time"),
                ("3 -", "Re-list Ingredients"),
            )
            for ele in options:
                print("\n   ", ele[0], ele[1])
            print()
            choice = int(input("Enter the number for desired update: "))
        # handle non-interger inputs
        except ValueError:
            print()
            print("*Only Intergers accepted")
        else:
            break`

    `cursor.execute(
        # first required parameter is sql query
        "SELECT name, cooking_time, ingredients FROM recipes WHERE id like %s",
        # MUST add "," at end...cursor.execute REQUIRES a tuple (or list, or dict) as second parameter
        (num,),
    )`

    `recipe = cursor.fetchall()`

    `# if statement for name update
    if choice == 1:
        print("\n-----------------------------------------")
        print("\nUpdating the Name of", recipe[0][0])
        print("\n-----------------------------------------")
        print()
        new_name = str(input(("Enter new name: ")))
        try:
            # query to update name
            cursor.execute(
                "UPDATE recipes SET name = %s WHERE id = %s",
                (
                    # f string used here
                    f"{new_name}",
                    num,
                ),
            )
        except:
            print()
            print("Oh no, something went wrong")
        else:
            conn.commit()
            print()
            print("Name has been updated.")`

    `# if statement for cooking time update
    if choice == 2:
        print("\n-----------------------------------------------")
        print("\nUpdating the Cooking Time of", recipe[0][0])
        print("\n-----------------------------------------------")
        print()
        new_cooking_time = int(input(("Enter new cooking time (in minutes): ")))
        # split ingredients so length can be determined for calc_difficulty
        ingredients = recipe[0][2].split(", ")
        # use new cooking time/old ingredients to determine difficulty
        new_difficulty = calc_difficulty(new_cooking_time, ingredients)
        try:
            # query to update cooking time and difficulty
            cursor.execute(
                "UPDATE recipes SET cooking_time = %s, difficulty = %s WHERE id = %s",
                (
                    # f string used here
                    f"{new_cooking_time}",
                    f"{new_difficulty}",
                    num,
                ),
            )
        except:
            print()
            print("Oh no, something went wrong")
        else:
            conn.commit()
            print()
            print("Cooking Time has been updated.")`

    `# if statement for ingredient update
    if choice == 3:
        print("\n--------------------------------------------------")
        print("\nRe-listing the Ingredients of ", recipe[0][0])
        print("\n--------------------------------------------------")
        print("\n*Keep in mind, all existing ingredients will be erased with update*")
        print()
        new_ingredients = []
        ingredient = input(
            "Write an ingredient and press enter, type 'done' when finished: "
        )
        # while loop to add ingredients
        while ingredient != "done":
            # add ingredient to list
            new_ingredients.append(ingredient.title())
            # request additional ingredients
            ingredient = input("Enter another ingredient, or type 'done' to finish: ")
        # use old cooking time and new ingredient list to calculate difficulty
        new_difficulty = calc_difficulty(recipe[0][1], new_ingredients)
        # convert list into comma seperated string
        # necessary because MySQL does not support arrays
        new_ingredients = ", ".join(new_ingredients)
        try:
            # query to update ingredients and difficulty
            cursor.execute(
                "UPDATE recipes SET ingredients = %s, difficulty = %s WHERE id = %s",
                (
                    # f string used here
                    f"{new_ingredients}",
                    f"{new_difficulty}",
                    num,
                ),
            )
        except:
            print()
            print("Oh no, something went wrong")
        else:
            conn.commit()
            print()
            print("Ingredients have been updated.")`

#### Deleting a Recipe with delete_recipe()

`def delete_recipe(conn, cursor):
    # query to get id/name of all recipes for display
    cursor.execute("SELECT id, name FROM recipes")`

    `results = cursor.fetchall()
    # print recipes
    for row in results:
        print(row[0], row[1])
        print()
    # put try else in while loop to isolate and prevent from impacting code flow
    while True:
        try:
            num = int(input("Enter the number for recipe to delete: "))
        # handle non-interger inputs
        except ValueError:
            print()
            print("*Only Intergers accepted")
        else:
            break
    # use num to query for specified recipe
    cursor.execute(
        # first required parameter is sql query
        "SELECT id, name FROM recipes WHERE id like %s",
        # MUST add "," at end...cursor.execute REQUIRES a tuple (or list, or dict) as second parameter
        (num,),
    )
    recipe = cursor.fetchall()
    recipe_id = recipe[0][0]
    recipe_name = recipe[0][1]`

    `print("\nx-----x-----x-----x-----x-----x-----x-----x-----x")
    print("\nAre you sure you want to delete", recipe_name, "?")
    print("\nx-----x-----x-----x-----x-----x-----x-----x-----x")
    print()
    # have user confirm delete before executing
    confirm = str(input("Type 'yes' to continue, or 'no' to cancel: "))
    # i fstatement for yes
    if confirm == "yes":
        try:
            cursor.execute(
                "DELETE FROM recipes WHERE id = %s",
                (f"{recipe_id}",),
            )
        except:
            print()
            print("Oh no, something went wrong")
        else:
            conn.commit()
            print()
            print("Recipe has been deleted.")
    # if statement for no
    if confirm == "no":
        print()
        print("Phew!")
        print()
        print("Nothing has been deleted.")
        print()`

