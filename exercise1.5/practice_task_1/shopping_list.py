class ShoppingList(object):
  def __init__(self, list_name):
    self.list_name = list_name
    self.shopping_list = []

  def add_item(self, item):
    txt = item.capitalize()
    if txt not in self.shopping_list:
      self.shopping_list.append(txt)
    else:
      print()
      print('Uh oh! ' + txt + " not added because it's already on the list.")

  def remove_item(self, item):
    choice = item.capitalize()
    if choice in self.shopping_list:
      self.shopping_list.remove(choice)

  def view_list(self):
    n = len(self.shopping_list)
    for i in range(0, n):
      print(' - ' + self.shopping_list[i])

pet_store_list = ShoppingList("Pet Store Shopping List")

print()
print(pet_store_list.list_name)

items = ['dog food', 'frisbee', 'bowl', 'collars', 'flea collars']

for i in items:
  pet_store_list.add_item(i)

print()
print('Original List: ')
pet_store_list.view_list()

pet_store_list.remove_item('flea collars')

pet_store_list.add_item('frisbee')

print()
print('Edited List: ')
pet_store_list.view_list()