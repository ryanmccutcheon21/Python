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
