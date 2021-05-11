amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
print(amazon_cart[0:2]) # ['notebooks', 'sunglasses']
print(amazon_cart[0::2]) # ['notebooks', 'toys']

# lists are mutable, meaning we can change a value in the list
amazon_cart[0] = 'laptop'
print(amazon_cart) # ['laptop', 'sunglasses', 'toys', grapes']
print(amazon_cart[0:3]) # ['laptop', 'sunglasses', 'toys']
print(amazon_cart) # ['laptop', 'sunglasses', 'toys', grapes']

amazon_cart[0] = 'laptop'
new_cart = amazon_cart
new_cart[0] = 'gum'
print(new_cart) # ['gum', 'sunglasses', 'toys', 'grapes']
print(amazon_cart) # ['gum', 'sunglasses', 'toys', 'grapes']
# new_cart changes amazon_cart because it assigns new_cart
# to the same reference in memory

# to create a copy of amazon_cart without assigning it to the 
# same refernce, use list slicing
# Example:
new_cart = amazon_cart[:]
# now amazon_cart will stay the same, and new_cart is a copy of
# amazon_cart with its own reference in memory