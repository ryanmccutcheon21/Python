def say_hello():
    print('Hello')


say_hello()
# Hello

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


def show_tree():
    fill = '*'
    empty = ' '
    for row in picture:
        for pixel in row:
            if pixel:
                print(fill, end='')
            else:
                print(empty, end='')
    print('')


show_tree()

#        *
#       ***
#      *****
#     *******
#        *
#        *


# Parameters and Arguments
def say_hello(name, emoji):
    print(f'Hello {name} {emoji}')


say_hello('Ryan', ':)')
# Hello Ryan :)

# keyword arguments
say_hello(emoji=':)', name='Kayla')
# Hello Kayla :)


# default parameters


def say_hello(name='Ryan', emoji=':)'):
    print('Hello {name} {emoji}')


say_hello()
# Hello Ryan :)


# return
def sum(num1, num2):
    num1 + num2


sum(4, 5)  # nothing shows when we run this
print(sum(4, 5))  # None


# We need the return keyword to return the value
def sum(num1, num2):
    return num1 + num2


print(sum(4, 5))  # 9
