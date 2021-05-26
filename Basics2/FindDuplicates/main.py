some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for val in some_list:
    if some_list.count(value) > 1:
        if val not in duplicates:
            duplicates.append(value)
print(duplicates)
# ['b', 'n']
