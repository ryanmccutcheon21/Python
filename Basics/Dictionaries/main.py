dictionary = {
    'a': [1, 2, 3],
    'b': 'Hello',
    'x': True
}

print(dictionary['b'])  # Hello
print(dictionary['c'])  # KeyError because 'c' is not a key
print(dictionary['a'][1])  # 2

my_list = [
    {
        'a': [1, 2, 3],
        'b': 'Hello',
        'x': True
    },
    {
        'a': [4, 5, 6],
        'b': 'Hello',
        'x': True
    }
]

print(my_list[0]['a'][2])  # 3
print(my_list[1]['a'][1])  # 5
