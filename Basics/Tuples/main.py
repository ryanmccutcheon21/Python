# Tuple
# think of them as an immutable list
my_tuple = (1, 2, 3, 4, 5)
my_tuple[1] = 'z'  # Error: 'tuple' object does not support item
# assignment
print(my_tuple[1])  # 2
print(5 in my_tuple)  # True

# a tuple is a valid key in a dictionary because it is immutable
user = {
    (1, 2, 3) = [1, 2, 3]
}
print(user[(1, 2)])  # [1,2,3]

new_tuple = my_tuple[1:2]
print(new_tuple)  # (2,)

tuple_3 = my_tuple[1:4]
print(tuple_3)  # (2.3,4)

x, y, z, *other = (1, 2, 3, 4, 5)
print(x)  # 1
print(z)  # 3
print(other)  # [4,5]


print(my_tuple.count(3))  # 1, because there is one 3 in my_tuple
print(my_tuple.index(4))  # 3
print(len(my_tuple))  # 5
