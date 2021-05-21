is_Friend = True
is_User = True

print(is_Friend and is_User)  # True

# if or is more performant than if else because the Python
# interpreter doesn't need to evaluate the second condition
# if the first is true
if is_Friend or is_User:
    print('best friends forever')
