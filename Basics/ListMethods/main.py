basket = [1, 2, 3, 4, 5]
print(len(basket)) # 5

# Adding
new_list = basket.append(6)
print(basket) # # [1, 2, 3, 4, 5, 6]
print(new_list) # None

# to make the above work to copy the appended basket and set
# it to new_list's value
basket.append(6)
new_list = basket
print(basket) # [1, 2, 3, 4, 5, 6]
print(new_list) # [1, 2, 3, 4, 5, 6]


# Insert
basket.insert(4, 100)
print(basket) # [1, 2, 3, 4, 100, 6]

new_list = basket.insert(4, 100)
print(basket) # [1, 2, 3, 4, 100, 6]
print(new_list) # None
# same as before in adding
# the method only adds to basket

# Extend
basket.extend([100])
print(basket) # [1, 2, 3, 4, 5, 6, 100]


# Removing
basket.pop()
print(basket) # [1, 2, 3, 4, 5, 6]
basket.pop(0) # [2, 3, 4, 5, 6]

basket.remove(4)
print(basket) # [2, 3, 5, 6]

new_list = basket.pop(2) # 5
# returns the value that was removed

new_list = basket.remove(2) # None

basket.clear()
print(basket) #
# It's empty

basket = ['a', 'b', 'c', 'd', 'e']
print(basket.index('d')) # 3 
print(basket.index('d', 0, 2)) # ValueError because we start looking
# at the index of 0 and stop at index of 2, and 'd' isn't between those 
# values

print('d' in basket) # True
print('x' in basket) # False

print('i' in 'Hi my name is Ryan') # True

print(basket.count('d')) # 1 because there is one 'd' in basket


alphabet = ['a', 'b', 'c', 'd', 'e', 'd']
print(alphabet.sort()) # None
alphabet.sort()
print(alphabet) # ['a', 'b', 'c', 'd', 'd', 'e']

print(sorted(alphabet)) # ['a', 'b', 'c', 'd', 'd', 'e']
print(alphabet) # ['a', 'b', 'c', 'd', 'e', 'd']
# sorted is a function instead of a method like sort
# it produces a new array, and does not change the original
# value of the object it's called on, in this case alphabet

new_alphabet = alphabet.copy() # ['a', 'b', 'c', 'd', 'e', 'd']
# returns a copy alphabet and assigns the values to new_alphabet
# but alphabet is unchanged

alphabet.reverse()
print(alphabet) # ['d', 'e', 'd', 'c', 'b', 'a']