# price_dict is a dictionary that will hold key:value pairs where the key is the item name (a string) and the value is the price (a float)
price_dict = {}

# cart is a string containing the contents of the shopping cart, one item per line
cart = ''

# total is the total dollar value of all the items in the cart
total = 0

'''
This function will read the contents of the store_db.txt file
and store each line as an item in the price_list dictionary.
'''
def import_price_list():
  pass

'''
This function accepts an item as the parameter, then adds the item
to the cart and updates the total value of the cart.
The keyword 'global' indicates to Python that when you modify the
values of cart and total you want to modify the variables that are
available to the whole program, not create a new variable just for
this function.
'''
def add_to_cart(item):
  pass


'''
In the main portion of your program you need to:
1. import the price list into the dictionary using import_price_list()
2. read the shopping list and add each item to the cart using add_to_cart()
3. output the contents of the cart and the total value of the cart
'''
