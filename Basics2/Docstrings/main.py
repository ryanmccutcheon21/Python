def test(a):
    # The following is a docstring and will show what we
    # write in the popup in the code editor explaining
    # what the function was/ or whatever we wrote to
    # describe the funciton
    '''
    Info: this function tests and prints param a
    '''
    print(a)


test('!!!!')
help(test)  # Info: this function tests and prints param a
# the help method is used to show our docstring to explain what
# the function does

print(test.__doc__)  # does the same thing as the help method
