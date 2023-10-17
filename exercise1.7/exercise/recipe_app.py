from sqlalchemy import create_engine

# establish connection to database
engine = create_engine("mysql://python-two:AnotherPassword@localhost/task_database")

# import declarative_base and generate class so it can be inherited
# changed from `sqlalchemy.ext.declarative` because of deprecated notice
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# import to be able to create a session
from sqlalchemy.orm import sessionmaker

# generate Session class and connect to engine using bind
Session = sessionmaker(bind=engine)
# initialize session object that will be used for all future operations in app
session = Session()

# import Column and data types
from sqlalchemy import Column

from sqlalchemy.types import Integer, String


# create table as a class - also referred to as a data model/model
# MUST inherit Base!
class Recipe(Base):
    # optional attribute, names created table
    __tablename__ = "final_recipes"
    # define attributes of model and have them create columns in table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # method that shows a quick representation of each recipe
    def __repr__(self):
        return (
            "<Recipe ID/Name: "
            + str(self.id)
            + "-"
            + self.name
            + "Diff: "
            + self.difficulty
            + ">"
        )

    # method that prints a well-formatted version of the recipe
    def __str__(self):
        list_ingredients = self.ingredients.split(", ")
        output = (
            "-" * 50
            + f"\n"
            + f"\nRecipe name: {self.name}"
            + f"\nCooking Time: {self.cooking_time} minutes"
            + f"\nDifficulty: {self.difficulty}"
            + "\nIngredients: \n"
        )
        for ingredient in list_ingredients:
            output += f"\t- {ingredient}\n"
        output
        return output

    # method to calculate difficulty of recipe
    def calculate_difficulty(self):
        ingredients = self.ingredients.split(", ")
        if self.cooking_time < 10 and len(ingredients) < 4:
            self.difficulty = "Easy"
        if self.cooking_time < 10 and len(ingredients) >= 4:
            self.difficulty = "Medium"
        if self.cooking_time >= 10 and len(ingredients) < 4:
            self.difficulty = "Intermediate"
        if self.cooking_time >= 10 and len(ingredients) >= 4:
            self.difficulty = "Hard"

    # method to retrieve ingredients as a list
    def return_ingredients_as_list(self):
        # no ingredients return empty list
        if len(self.ingredients == 0):
            return []
        # split ingredients into a list
        else:
            return self.ingredients.split(", ")


# create_all method must be used to create tables of all defined models
Base.metadata.create_all(engine)


def create_recipe():
    try:
        # collect name from user
        name = str(input("\nEnter recipe name: ")).title()
        # validate length of name
        while len(name) > 50:
            print("\n\t*Error: Name must be 50 characters or less*")
            name = str(input("\nEnter recipe name: "))

        # collect cooking_time from user
        cooking_time = input("\nEnter cooking time (in mintues): ")
        # validate it is numeric
        while not cooking_time.isnumeric():
            print("\n\t*Error: Cooking must be a numeric value")
            cooking_time = input("\nEnter cooking time (in mintues): ")
        # convert entry to integer
        cooking_time = int(cooking_time)
        # collect ingredients from user
        ingredients = []
        num = input("\nEnter the number of ingredients in the recipe: ")
        # validate entry is numeric
        while not num.isnumeric():
            print("\n\t*Error: number of ingredients must be a numeric value")
            num = input("\nEnter the number of ingredients in the recipe: ")
        # convert entry to integer
        num = int(num)
        # run for loop to get ingredients from user
        for ingredient in range(num):
            ingredient = str(input("\nEnter ingredient: ")).capitalize()
            # validate entry is alphabetical
            while not any(c for c in ingredient if c.isalpha() or c.isspace()):
                print(
                    "\n\t*Error: Ingredients can only contain alphabetic characters or spaces"
                )
                ingredient = str(input("\nEnter ingredient: ")).capitalize()
            ingredients.append(ingredient)
        # convert list into comma seperated string
        # necessary because MySQL does not support arrays
        ingredients = ", ".join(ingredients)
        # create Recipe object using Recipe model
        recipe_entry = Recipe(
            name=name, cooking_time=cooking_time, ingredients=ingredients
        )

        # call built in method to calculate difficulty
        recipe_entry.calculate_difficulty()
        # add recipe to database
        session.add(recipe_entry)
        # commit changes
        session.commit()
        # inform user of successful add
        print()
        print("\n\tRecipe added successfully!")
        print()
        main_menu()

    # error handling: alert user if something has gone wrong
    except Exception as e:
        print("\nThere was an error creating the recipe...")
        print(e)
        print()
        main_menu()


def view_all_recipes():
    # query database for all recipes
    recipes_list = session.query(Recipe).all()
    # if no recipes exist inform user
    if len(recipes_list) == 0:
        print("\n\tLooks like there are no recipes on the list...")
        print("\n\tBetter add some!")
    # print all found recipes
    else:
        print()
        print("*" * 6 + "All recipes in databse" + "*" * 6)
        for recipe in recipes_list:
            print(recipe)
        main_menu()


def search_by_ingredients():
    # query database to count number of stored recipes
    recipe_count = session.query(Recipe).count()
    # if no recipes in database alert user
    if recipe_count == 0:
        print("\n\tLooks like there are no recipes on the list...")
        print("\n\tBetter add some!")
        print()
        main_menu()
    # query database for all ingredient rows
    results = session.query(Recipe.ingredients).all()
    # initialize empty ingredients list
    all_ingredients = []
    # loop to populate ingredient list
    for result in results:
        # split strings received from database
        temp_list = result[0].split(", ")
        # loop temp list to add ingredients to main list
        for item in temp_list:
            if item not in all_ingredients:
                all_ingredients.append(item)

    # add numbers to all ingredients list (starting at 1)
    lst = enumerate(all_ingredients, 1)
    # reconstruct as a list
    numbered_lst = list(lst)
    # provide list to user
    print("\nAll Ingredients in database: ")
    # loop numbered list and print all elements
    for ingredient in numbered_lst:
        print(f"\n\t{ingredient[0]} {ingredient[1]}")
    # initialize empty options list
    options = []
    # fill options list with numbers from numbered list
    for item in numbered_lst:
        num = item[0]
        options.append(num)
    # prompt user to select ingredients they would like to search
    selected = input(
        "\nEnter number assigned to each ingredient you want to search (seperated by spaces): "
    ).split()
    # initialize empty search ingredients list
    search_ingredients = []
    # loop input from user to validate
    for i in selected:
        # if entry is not numeric/doesnt match the options list throw an error
        if not i.isnumeric() or int(i) not in options:
            print("\n\t*Error: Only numeric values that match an ingredient accepted.")
            print("\n\tPlease try again.")
            return None
        # populate search ingredients list with names of ingredients
        else:
            i = int(i)
            ingredient = numbered_lst[i - 1][1]
            search_ingredients.append(ingredient)
    # initialize empty condition list
    condition_list = []
    # loop search ingredients to populate condition list
    for ingredient in search_ingredients:
        # create like term (needs to be string surrounded by %)
        like_term = str(f"%{ingredient}%")
        condition_list.append(Recipe.ingredients.like(like_term))
    # use condition list to query database for ingredients that match search parameters
    matching_recipes = session.query(Recipe).filter(*condition_list).all()
    # inform user if no matches
    if len(matching_recipes) == 0:
        print("\n\tOh no, looks like no recipes matched your search. :(")
        main_menu()
    # provide matching recipes to user
    else:
        print("\nMatching Recipes: ")
        print()
        # loop query response and print recipe strings
        for recipe in matching_recipes:
            print(recipe)
        print()
        main_menu()


def edit_recipe():
    # query database to count number of stored recipes
    recipe_count = session.query(Recipe).count()
    # if no recipes in database alert user
    if recipe_count == 0:
        print("\n\tLooks like there are no recipes on the list...")
        print("\n\tBetter add some!")
        print()
        main_menu()
    # get all recipes from database
    results = session.query(Recipe.id, Recipe.name).all()
    # initialize empty options list
    options = []
    print("\nAll Recipes in database:")
    # display all recipes and their IDs
    for result in results:
        print(f"\n\tID: {result[0]} - {result[1]}")
        # populate options list with ID of all recipes
        options.append(result[0])
    # collect ID for choosen recipe from user
    choosen = input("\nEnter the ID of the recipe you'd like to edit: ")
    # validate entry is numeric
    while not choosen.isnumeric():
        print("\n\t*Error: ID must be a numeric value")
        choosen = input("\nEnter the ID of the recipe you'd like to edit: ")
    # convert entry into integer
    choosen = int(choosen)
    # confirm entry in options list
    if choosen not in options:
        print("\n\tOh no, looks like there was no recipe that matched this ID. :(")
        print("\n\tYou'll have to try again.")
        main_menu()
    # query databade for recipe to be edited
    recipe_to_edit = session.query(Recipe).filter(Recipe.id == choosen).one()
    print()
    print("-" * 70)
    # present recipe to be edited to user
    print("\nRecipe that will be edited: ")
    print(f"\n\t1.  Name: {recipe_to_edit.name}")
    print(f"\n\t2.  Cooking Time: {recipe_to_edit.cooking_time}")
    print(f"\n\t3.  Ingredients: {recipe_to_edit.ingredients}")
    print()
    print("-" * 70)
    # create list of options user can select to edit
    edit_options = [1, 2, 3]
    # have user determine what row they would like to edit
    row_to_edit = input(
        "\nEnter the number matching the recipe attribute you'd like to edit: "
    )
    # confirm user input is numeric
    while not row_to_edit.isnumeric():
        print("\n\t*Error: Choice must be a numeric value")
        row_to_edit = input(
            "\nEnter the number matching the recipe attribute you'd like to edit: "
        )
    # convert choice to integer
    row_to_edit = int(row_to_edit)
    # validate input is in options list
    if row_to_edit not in edit_options:
        print(
            "\n\tOh no, looks like there was no attribute that matched your choice. :("
        )
        print("\n\tYou'll have to try again.")
        main_menu()
    # code for editing "name" row
    if row_to_edit == 1:
        print()
        print("-" * 50)
        print(f"\nUpdating name of {recipe_to_edit.name}")
        print()
        print("-" * 50)
        # collect new name from user
        new_name = str(input("\nEnter the new name: ")).title()
        # validate it is not too long
        while len(new_name) > 50:
            print("\n\t*Error: Name must be 50 characters or less*")
            new_name = str(input("\nEnter the new name: "))
        # update name of selected recipe in database
        try:
            session.query(Recipe).filter(Recipe.id == choosen).update(
                {Recipe.name: new_name}
            )
            # commit changes
            session.commit()
            # inform user of successful update
            print()
            print("\n\tRecipe updated successfully!")
            print()
            main_menu()

        # error handling: alert user if something has gone wrong
        except Exception as e:
            print("\nThere was an error updating the recipe...")
            print(e)
            print()
            main_menu()
    # code for editing "cooking_time" row
    elif row_to_edit == 2:
        print()
        print("-" * 50)
        print(f"\nUpdating the cooking time of {recipe_to_edit.name}")
        print()
        print("-" * 50)
        # collect new cooking time from user
        new_time = input("\nEnter cooking time (in mintues): ")
        # validate it is numeric
        while not new_time.isnumeric():
            print("\n\t*Error: Cooking must be a numeric value")
            new_time = input("\nEnter cooking time (in mintues): ")
        # convert cooking time to int
        new_time = int(new_time)
        try:
            # create new recipe with updated cooking time to be able to run calcuate difficulty
            recipe_update = Recipe(
                name=recipe_to_edit.name,
                cooking_time=new_time,
                ingredients=recipe_to_edit.ingredients,
            )
            # calculate difficulty with updated recipe data
            recipe_update.calculate_difficulty()
            # update cooking time and difficulty in database for recipe
            session.query(Recipe).filter(Recipe.id == choosen).update(
                {
                    Recipe.cooking_time: new_time,
                    Recipe.difficulty: recipe_update.difficulty,
                }
            )
            # commit changes
            session.commit()
            # inform user of successful update
            print()
            print("\n\tRecipe updated successfully!")
            print()
            main_menu()

        # error handling: alert user if something has gone wrong
        except Exception as e:
            print("\nThere was an error updating the recipe...")
            print(e)
            print()
            main_menu()
    # code for editing "ingredients" row
    else:
        print()
        print("-" * 50)
        print(f"\nUpdating the ingredients of {recipe_to_edit.name}")
        print(
            "\n\t***Note: All current ingredients will be replaced by the new entry***"
        )
        print()
        print("-" * 50)
        # initialize new empty ingredients list
        new_ingredients = []
        # get number of new ingredients from user
        num = input("\nEnter the number of ingredients in the recipe: ")
        # validate entry is numeric
        while not num.isnumeric():
            print("\n\t*Error: number of ingredients must be a numeric value")
            num = input("\nEnter the number of ingredients in the recipe: ")
        # convert entry to integer
        num = int(num)
        try:
            # run for loop to get ingredients from user
            for ingredient in range(num):
                ingredient = str(input("\nEnter ingredient: ")).capitalize()
                # validate entry is alphabetical
                while not any(c for c in ingredient if c.isalpha() or c.isspace()):
                    print(
                        "\n\t*Error: Ingredients can only contain alphabetic characters or spaces"
                    )
                    ingredient = str(input("\nEnter ingredient: ")).capitalize()
                # add ingredient to new list
                new_ingredients.append(ingredient)
            # convert list into comma seperated string
            # necessary because MySQL does not support arrays
            new_ingredients = ", ".join(new_ingredients)
            # create new recipe with updated ingredients to be able to run calcuate difficulty
            recipe_update = Recipe(
                name=recipe_to_edit.name,
                cooking_time=recipe_to_edit.cooking_time,
                ingredients=new_ingredients,
            )
            # call built in method to calculate difficulty
            recipe_update.calculate_difficulty()
            # update ingredients and difficulty for recipe in database
            session.query(Recipe).filter(Recipe.id == choosen).update(
                {
                    Recipe.ingredients: new_ingredients,
                    Recipe.difficulty: recipe_update.difficulty,
                }
            )
            # commit changes
            session.commit()
            # inform user of successful update
            print()
            print("\n\tRecipe updated successfully!")
            print()
            main_menu()
        # error handling: alert user if something has gone wrong
        except Exception as e:
            print("\nThere was an error updating the recipe...")
            print(e)
            print()
            main_menu()


def delete_recipe():
    # query database to count number of stored recipes
    recipe_count = session.query(Recipe).count()
    # if no recipes in database alert user
    if recipe_count == 0:
        print("\n\tLooks like there are no recipes on the list...")
        print("\n\tBetter add some!")
        print()
        main_menu()
    # get all recipes
    results = session.query(Recipe.id, Recipe.name).all()
    # initialize empty options list
    options = []
    print("\nAll Recipes in database:")
    # loop to print all recipes, displaying ID
    for result in results:
        print(f"\n\tID: {result[0]} - {result[1]}")
        options.append(result[0])
    # prompt user to input desired ID
    choosen = input("\nEnter the ID of the recipe you'd like to delete: ")
    # check input is numeric
    while not choosen.isnumeric():
        print("\n\t*Error: ID must be a numeric value")
        choosen = input("\nEnter the ID of the recipe you'd like to edit: ")
    # convert input into integer
    choosen = int(choosen)
    # confirm input matches a displayed recipe
    if choosen not in options:
        print("\n\tOh no, looks like there was no recipe that matched this ID. :(")
        print("\n\tYou'll have to try again.")
        main_menu()
    # query DB for recipe to be deleted
    to_delete = session.query(Recipe).filter(Recipe.id == choosen).one()
    print("\nAre you sure you'd like to delete the following recipe: ")
    print()
    print(to_delete)
    print("-" * 50)
    # ask user to confirm deletion
    confirmation = str(input("\nEnter 'yes' to delete or 'no' to cancel: ")).lower()
    # validate that input is either yes or no
    while (not confirmation == "yes") and (not confirmation == "no"):
        print("\n\t*Error - only 'yes' or 'no' are acceptable entries*")
        confirmation = str(input("\nEnter 'yes' to delete or 'no' to cancel: ")).lower()
    # return to main menu with out deleting anything for no answer
    if confirmation == "no":
        print("\n\tClose call...")
        print("\n\t...but nothing was deleted. Phew!")
        main_menu()
    # delete recipe and return to main menu for yes answer
    else:
        try:
            session.delete(to_delete)
            session.commit()
            print()
            print("\n\tRecipe has been successfully deleted.")
            print()
            main_menu()
        # error handling: alert user if something has gone wrong
        except Exception as e:
            print("\nThere was an error deleting the recipe...")
            print(e)
            print()
            main_menu()


def main_menu():
    # initialize blank choice variable
    choice = ""
    # greet user and print menu
    print()
    print("-" * 50)
    print("\nWelcome to the Recipe App Main Menu?")
    print("\nEnter the prompt matching your choice below: ")
    print("\n\t1 - Create a Recipe")
    print("\n\t2 - View all Recipes")
    print("\n\t3 - Search for a Recipe")
    print("\n\t4 - Edit a Recipe")
    print("\n\t5 - Delete a Recipe")
    print("\n   'quit' - Close application")
    print()
    print("-" * 50)
    # prompt user to enter choice
    choice = str(input("\nWhat would you like to do? "))
    # while loop to keep menu appearing unless choice is quit
    while choice != "quit":
        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredients()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        # else handles any entry that does not match a function/is quit
        else:
            print(
                "\n\tOh no, looks like there is no option that matches that choice. :("
            )
            print("\n\tYou'll have to try again.")
            main_menu()
    # say goodbye to user and close application
    print("\n\tGoodbye")
    session.close()
    engine.dispose()
    exit()


# call main menu function to start app
main_menu()
