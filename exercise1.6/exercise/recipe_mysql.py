# set-up section of code
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="python-two", passwd="AnotherPassword"
)

cursor = conn.cursor()
# create db (checks if it exists first)
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
# needed to use specified db
cursor.execute("USE task_database")
# creates recipes table (checks is it exists first)
cursor.execute(
    """CREATE TABLE IF NOT EXISTS recipes(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  ingredients VARCHAR(255),
  cooking_time INT,
  difficulty VARCHAR(20)      
)"""
)


# functions section of code


def create_recipe(conn, cursor):
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

    difficulty = calc_difficulty(cooking_time, ingredients)

    # NEED to convert AFTER calculating difficulty otherwise it will not measure the length of the list
    # convert list into comma seperated string
    # necessary because MySQL does not support arrays
    ingredients = ", ".join(ingredients)

    cursor.execute(
        "INSERT INTO recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)",
        # specifying values to be added to database
        (name, ingredients, cooking_time, difficulty),
    )
    # commit recipe to database
    conn.commit()
    print()
    print("Recipe has been added!")


# moved outside of create recipe so it can be accessed by update recipe
def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    if cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    if cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    if cooking_time >= 10 and len(ingredients) >= 4:
        return "Hard"


def search_recipe(conn, cursor):
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
            print("Ingredients:", row[3])


def update_recipe(conn, cursor):
    cursor.execute("SELECT id, name FROM recipes")

    results = cursor.fetchall()

    for row in results:
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
            break

    cursor.execute(
        # first required parameter is sql query
        "SELECT name, cooking_time, ingredients FROM recipes WHERE id like %s",
        # MUST add "," at end...cursor.execute REQUIRES a tuple (or list, or dict) as second parameter
        (num,),
    )

    recipe = cursor.fetchall()

    # if statement for name update
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
            print("Name has been updated.")

    # if statement for cooking time update
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
            print("Cooking Time has been updated.")

    # if statement for ingredient update
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
            print("Ingredients have been updated.")


def delete_recipe(conn, cursor):
    # query to get id/name of all recipes for display
    cursor.execute("SELECT id, name FROM recipes")

    results = cursor.fetchall()
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
    recipe_name = recipe[0][1]

    print("\nx-----x-----x-----x-----x-----x-----x-----x-----x")
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
        print()


def quit_app(conn, cursor):
    conn.commit()
    conn.close()


# main menu function
def main_menu(conn, cursor):
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
        print()

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "quit":
            quit_app(conn, cursor)


main_menu(conn, cursor)
