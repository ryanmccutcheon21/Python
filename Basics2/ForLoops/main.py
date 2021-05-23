for item in 'Zero to Mastery':
    print(item)
# Z
# e
# r
# o

# t
# o

# M
# a
# s
# t
# e
# r
# y

for item in [1, 2, 3]:
    print(item)
# 1
# 2
# 3

for item in {1, 2, 3}:
    print(item)
# 1
# 2
# 3

for item in (1, 2, 3):
    print(item)
# 1
# 2
# 3


user = {
    'name': 'Ryan',
    'age': 26,
    'can_swim': True
}

for item in user:
    print(item)
# name
# age
# can_swim

for item in user.items():
    print(item)
# ('name', 'Ryan')
# ('age', 26)
# ('can_swim', True)

for item in user.values():
    print(item)
# Ryan
# 26
# True

for item in user.keys():
    print(item)
# name
# age
# can_swim

for item in user.items():
    key, value = item
    print(key, value)
# name Ryan
# age 26
# can_swim True

# Shorthand way of last example
for key, value in user.items():
    print(key, value)
# name Ryan
# age 26
# can_swim True


# Tricky counter exercise
# loop over the list and return the sum total of the list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

counter = 0
for item in my_list:
    counter += item

print(counter)  # 55


# range()
print(range(100))  # range(0, 100)
# looks like a tuple but it's a range object

for number in range(100):
    print(number)
# prints numbers 0 - 99

for _ in range(0, 10, 2):
    print(_)
# 0 2 4 6 8
# the third param is the stepover value

for _ in range(10, 0, -1):
    print(_)
# 10 9 8 7 6 5 4 3 2 1
