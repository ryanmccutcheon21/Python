selfish = '01234567'

selfish = 100
print(selfish) # 100

selfish[0] = '8'
print(selfish) # returns a type error because a string is
# immutable and can't be changed unless it's value is completely
# reassigned