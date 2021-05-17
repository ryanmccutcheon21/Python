dictionary = {
    'weapons': [1, 2, 3],
    'greeting': 'hello',
    'is_Magic': True,
    123: [2, 3, 4],
    True: 'hey, bro',
    [100]: True,
    '1': [5, 6, 7],
    '1': 'same name as other key'
}

print(dictionary[123])  # [2,3,4]
print(dictionary[True])  # hey, bro
print(dictionary[100])  # unhashable type error
# a key needs to be immutable
print(dictionary['1'])  # same name as other key
# a key has to be unique
