my_set = {1, 2, 3, 4, 5}
print(my_set)  # {1, 2, 3, 4, 5}
my_set2 = {1, 2, 3, 4, 5, 5}
print(my_set2)  # {1, 2, 3, 4, 5}
# no duplicates in a set, everyhting has to be unique
my_set.add(7)
print(my_set)  # {1, 2, 3, 4, 5, 7}

# say you want to make a list only have unique values
# you can convert it to a set
my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))  # {1,2,3,4,5}

# sets do not support indexing
# print(my_set[0])  # TypeError


# Set Methods
this_is_a_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(this_is_a_set.difference(your_set))  # {1,2,3}
print(this_is_a_set.discard(5))  # None
print(this_is_a_set)  # {1,2,3,4}
print(this_is_a_set.difference_update(your_set))  # None
print(this_is_a_set)  # {1,2,3}

another_set = {1, 2, 3, 4, 5}
print(another_set.intersection(your_set))  # {4,5}

# shorthand for intersection method
print(another_set & your_set)  # {4,5}

print(another_set.isdisjoint(your_set))  # False

again_set = {1, 2, 3}
print(again_set.isdisjoint(your_set))  # True because none of the
# values match

print(again_set.union(your_set))  # {1,2,3,4,5,6,7,8,9,10}
# adds the sets together and removes duplicates

# shorthand for the union method
print(again_set | your_set)  # {1,2,3,4,5,6,7,8,9,10}

fourth_set = {4, 5}
print(fourth_set.issubset(your_set))  # True because all the values
# of fourth_set are in your_set

print(fourth_set.issuperset(your_set))  # False
print(your_set.issuperset(fourth_set))  # True because your_set
# ecompasses everything fourth_set has
