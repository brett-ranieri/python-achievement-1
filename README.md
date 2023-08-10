# Exercise 1

## Install Python

Install Python 3.8.7 and check for appropriate version by running `python --version`

## Setup Virtual Environment

Run the following command to create a new virtual environment `mkvirtualenv cf-python-base`

## Create Python Script

Open VsCode and create a file named add.py. In this file write simple code asking user to input two numbers, each assigned to their own variable. Once received have script add numbers together and return the answer as a third variable. Then print the solution.

## Setup ipython Shell

Install ipython with the following command `pip install ipython` then test ipython shell bu running `ipython`

## Export Requirements File

Use `pip freeze > requirements.txt` to create a requirements file. Then create a new environment named `cf-python-copy`. Finally, within the new environment run `pip install -r requirements.txt`

# Exercise 2

## Create a template recipe structure

A dictionary makes the most sense for an individual recipe becuase of it's built in key:value structure that matches the requirements of the recipe. It will support manipulation and access to the recipe data which will be useful for future interactions.

## Create Tea recipe following key:value prompts in exercise

`In [1]: recipe_1 = {
   ...: 'name': 'Tea',
   ...: 'cooking_time' : 5,
   ...: 'ingredients' : ['Tea leaves', 'Sugar', 'Water']
   ...: }`

## Create an outer structure in which to store recipes

A list makes sense for this structue as it is an ordered sequence built into Python, fulfilling the first part of the brief. Lists are also mutable, allowing for all of their internal elements to be modified or deleted as needed, which is also specified in the brief. 

## Create more recipes to fill all_recipes list 

Additional recipes are similar top structure for Tea recipe shown above. Add to all_recipes with append `all_recipes.append(recipe_2)`

## Print ingredients of each recipe as their own list

Ingredients are built as a list within the structure, so just need to print for each recipe `print(all_recipes[0]['ingredients']`
