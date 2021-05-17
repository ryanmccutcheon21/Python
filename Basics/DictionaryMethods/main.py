user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'other_age': 20
}

print(user['age'])  # key error because age does not exist
print(user.get('age'))  # None
print(user.get('age', 55))  # 55, because 55 was set as the default
# value
print(user.get('other_age', 55))  # 20, if it has a value that is what
# will be returned no matter what the default is
print('basket' in user)  # True
print('size' in user)  # False
print('hello' in user.keys())  # False
print('other_age' in user.keys())  # True
print('hello' in user.values())  # True
print(user.items())
# [('basket': [1, 2, 3]), ('greet': 'hello'), ('other_age': 20)]

user2 = user.copy()
print(user)
# {
#     'basket': [1, 2, 3],
#     'greet': 'hello',
#     'other_age': 20
# }
print(user2)
# {
#     'basket': [1, 2, 3],
#     'greet': 'hello',
#     'other_age': 20
# }

print(user.pop('other_age'))  # 20
# if you print user now, other_age is not in it anymore after
# popping it off the user dictionary

print(user.popitem())  # ('greet': 'hello')
# returns and removes a random item from the dictionary

print(user.update({'other_age': 55}))  # now the user dictionary
# other_age is set to 55


user.clear()
print(user)  # {}

# another way to create a dictionary
user2 = dict(name='Ryan')
print(user2)  # {'name': 'Ryan'}
