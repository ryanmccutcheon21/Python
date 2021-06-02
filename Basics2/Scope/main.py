# Scope - what variables do I have access to?
# Python has functional scope
if True:
    x = 10


def some_function():
    total = 100


print(x)  # 10
print(total)  # Error because we don't have access to total in the
# global scope


# Scope Rules
a = 1


def confusion():
    a = 5
    return a


print(confusion())  # 5
print(a)  # 1


# if a wasn't defined in confusion, then 1 would've been returned


# 1 - start with local
# 2 - Parent local?
# 3 - Global
# 4 - built in python functions


a = 1


def parent():
    a = 10

    def confusion():
        return a
    return confusion()


print(parent())  # 10
print(a)  # 1


# Global keyword
total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())  # 3

# A better way
total = 0


def count(total):
    total += 1
    return total


print(count(count(count(total))))  # 3


# Nonlocal keyword
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
# inner: nonlocal
# outer: nonlocal
