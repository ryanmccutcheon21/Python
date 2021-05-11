birth_year = input('What year were you born?')
age = 2021 - birth_year
print(f'Your age is {age}') # returns a TypeError because 
# birth_year is a string

birth_year = input('What year were you born?')
age = 2021 - int(birth_year)
print(f'Your age is {age}') # works because we converted birth_year
# back to an int