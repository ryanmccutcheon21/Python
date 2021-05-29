# *args **kwargs

def super_func(args):
    return sum(args)


super_func(1, 2, 3, 4, 5)  # TypeError: super_func() takes one
# positional argument, but 5 were given


def super_func(*args):
    return sum(args)


print(super_func(1, 2, 3, 4, 5))  # 15


def super_func(*args, **kwargs):
    print(kwargs)
    return sum(args)


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))
# {'num1': 5, 'num2': 10}
# 15


def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))  # 30


# Rule: params, *args, default parameters, **kwargs
# Example:
# def super_func(name, *args, i='hi', **kwargs):
