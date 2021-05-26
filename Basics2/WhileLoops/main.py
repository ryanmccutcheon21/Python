i = 0
while i < 50:
    print(i)
    break
# 0

while i < 50:
    print(i)
    i += 1
# prints numbers 0 - 49
else:
    print('done with all the work')
# 0 - 49
# done with all the work

while True:
    response = input('say something: ')
    if (response == 'bye'):
        break
# asks for an input with say something until the user inputs bye

my_list = [1, 2, 3]
for item in my_list:
    print(item)
    break
# 1


i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    break
# 1

my_list = [1, 2, 3]
for item in my_list:
    print(item)
    continue
# 1
# 2
# 3

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue
# 1
# 2
# 3
