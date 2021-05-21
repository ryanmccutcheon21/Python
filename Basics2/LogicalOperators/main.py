# Logical Operators
# >
# <
# ==
# >=
# <=
# !=
# and
# not
# or

print(4 > 5)  # False
print(4 == 5)  # False
print(not(1 == 1))  # False

is_magician = False
is_expert = True

# check if magician AND expert: 'You are a master magician'
if is_magician and is_expert:
    print('You are a master magician')

# check if magician BUT not expert: 'At least you're getting there'
elif is_magician and not is_expert:
    print("At least you're getting there")

# if you're not a magician: 'You need magic powers'
elif not is_magician:
    print("You need magic powers")

else:
    print("No options matched")
