import pickle


def display_recipe(recipe):
    print("")
    print("Recipe: ", recipe["name"])
    print("Cooking Time (mins): ", recipe["cooking_time"])
    print("Ingredients: ")
    for ele in recipe["ingredients"]:
        print("- ", ele)
    print("Difficulty: ", recipe["difficulty"])
    print("")


# function to search ingredients
def search_ingredients(data):
    # adds number to each element  in list
    lst = enumerate(data["all_ingredients"])
    # structures enumerated data into a list
    numbered_lst = list(lst)
    print("Ingredients List: ")
    # prints number and ingredient name for each element in list
    for ele in numbered_lst:
        print(ele[0], ele[1])
    try:
        # asks user to choose ingredient
        num = int(input("Enter number for ingredient you would like to search: "))
        ingredient_searched = numbered_lst[num][1]
        print("Searching for...", ingredient_searched, "...")
    except ValueError:
        print("Only Intergers accepted")
    except:
        print(
            "Oops, your input didn't match the allowed options. Make sure you choose a number that matches an ingredient on the list"
        )
    else:
        # loops recipe list to check ingredients, prints recipe if ingredient included
        for ele in data["recipes_list"]:
            if ingredient_searched in ele["ingredients"]:
                print(ele)


# user provides filename
filename = input("Enter filename where you've stored your recipes: ")
# open file and load with pickle
try:
    file = open(filename, "rb")
    data = pickle.load(file)
    print("File loaded successfully!")
# if file not found inform user
except FileNotFoundError:
    print("No files match that name - please try again")
# if unexpected error inform user
except:
    print("Oops, there was an unexpected error")
else:
    file.close()
    search_ingredients(data)

# test_data = {
#     "recipes_list": [
#         {
#             "name": "Tea",
#             "cooking_time": 5,
#             "ingredients": ["Water", "Tea", "Sugar", "Milk"],
#             "difficulty": "Medium",
#         },
#         {
#             "name": "Pasta",
#             "cooking_time": 20,
#             "ingredients": ["Pasta", "Tomato Sauce", "Cheese", "Bread"],
#             "difficulty": "Hard",
#         },
#         {
#             "name": "Third recipe",
#             "cooking_time": 30,
#             "ingredients": ["Bread", "Cheese", "Eggs", "Butter"],
#             "difficulty": "Hard",
#         },
#         {
#             "name": "Fourth nachos",
#             "cooking_time": 10,
#             "ingredients": ["Nacho Cheese", "Chips", "Salsa", "Jalapenos"],
#             "difficulty": "Hard",
#         },
#     ],
#     "all_ingredients": [
#         "Water",
#         "Tea",
#         "Sugar",
#         "Milk",
#         "Pasta",
#         "Tomato Sauce",
#         "Cheese",
#         "Bread",
#         "Eggs",
#         "Butter",
#         "Nacho Cheese",
#         "Chips",
#         "Salsa",
#         "Jalapenos",
#     ],
# }
