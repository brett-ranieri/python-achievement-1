recipes_list = []
ingredients_list = []

def take_recipe():
    name = str(input("Enter recipe name: "))
    cooking_time = int(input("Enter total cooking time: "))
    ingredients = str(input("Enter ingredients, each seperated by a comma: ")).split(", ")
    ingredients = [i.title() for i in ingredients]
    recipe = {
      "name": name.capitalize(),
      "cooking_time": cooking_time,
      "ingredients": ingredients
    }
    return(recipe)

n = int(input("How many recipes would you like to enter: "))

for i in range(0,n):
    recipe = take_recipe()
    for ele in recipe['ingredients']:
      if ele not in ingredients_list:
        ingredients_list.append(ele)
    recipes_list.append(recipe)

for recipe in recipes_list:
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
    print('')

ingredients_list.sort()
print('-----------------------------------')
print('Ingredients Used Across All Recipes')
print('-----------------------------------')
for ele in ingredients_list:
  print('-', ele)
