class Recipe(object):
  all_ingredients = []
  
  def __init__(self, name):
    self.name = name
    self.ingredients = []
    self.cooking_time = 0
    self.difficulty = "Need cooking time and ingredients to determine difficulty"

  def get_name(self):
    output = "Recipe Name: " + str(self.name)
    return output
  
  def get_cooking_time(self):
    output = "Cooking Time: " + str(self.cooking_time)
    return output
  
  def set_name(self):
    self.name = str(input("Enter Recipe name: "))

  def set_cooking_time(self, cooking_time):
    self.cooking_time = int(cooking_time)
    Recipe.calculate_difficulty(self)

  def add_ingredients(self, *ingredients):
    for ingredient in ingredients:
      if ingredient not in self.ingredients:
        self.ingredients.append(ingredient)
    Recipe.update_all_ingredients(self)
    Recipe.calculate_difficulty(self)

  def get_ingredients(self):
    output = "\nList of Ingredients: \n"
    for ingredient in self.ingredients:
      output += " - " + ingredient + "\n"
    return output
  
  def calculate_difficulty(self):
    if self.cooking_time < 10 and self.cooking_time > 0 and len(self.ingredients) < 4 and len(self.ingredients) > 0:
      self.difficulty = "Easy"
    if self.cooking_time < 10 and len(self.ingredients) >= 4:
      self.difficulty = "Medium"
    if self.cooking_time >= 10 and len(self.ingredients) < 4:
      self.difficulty = "Intermediate"
    if self.cooking_time >= 10 and len(self.ingredients) >= 4:
      self.difficulty = "Hard"

  def get_difficulty(self):
    if self.difficulty == None:
      difficulty = Recipe.calculate_difficulty(self)
      output = "Recipe difficulty: " + str(difficulty)
      return output
    else:
      output = "Recipe difficulty: " + str(self.difficulty)
      return output
    
  def search_ingredient(self, ingredient):
    return ingredient in self.ingredients
  
  def update_all_ingredients(self):
    for ingredient in self.ingredients:
      if ingredient not in Recipe.all_ingredients:
        Recipe.all_ingredients.append(ingredient)

  def __str__(self):
    output = "\nRecipe Name: " + str(self.name) + "\nCooking Time: " + str(self.cooking_time) + " minutes" + "\nDifficulty: " + str(self.difficulty) + "\nIngredients: \n"
    for ingredient in self.ingredients:
      output += " - " + ingredient + "\n"
    return output
  
def recipe_search(data, search_term):
  print("Searching...")
  for recipe in data:
    if recipe.search_ingredient(search_term):
      print(recipe)

tea = Recipe("Tea")
tea.set_cooking_time(5)
tea.add_ingredients("Tea", "Leaves", "Sugar", "Water")
print(tea)

coffee = Recipe("Coffee")
coffee.set_cooking_time(5)
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
print(coffee)

cake = Recipe("Cake")
cake.set_cooking_time(50)
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
print(cake)

banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.set_cooking_time(5)
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
print(banana_smoothie)

recipes_list = [tea, coffee, cake, banana_smoothie]

print()
print("Search test 1: Water")
recipe_search(recipes_list, "Water")

print()
print("Search test 2: Sugar")
recipe_search(recipes_list, "Sugar")

print()
print("Search test 3: Bananas")
recipe_search(recipes_list, "Bananas")

  
  
