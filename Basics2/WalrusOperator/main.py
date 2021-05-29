a = 'helloooooooooo'

if (len(a) > 10):
    print(f"too long {len(a)} elements")
# too long 14 elements


# With the Walrus operator
if ((n := len(a)) > 10):
    print(f"too long {n} elements")
# too long 14 elements


while((n := len(a)) > 1):
    print(n)
    a = a[:-1]
# 14
# 13
# 12
# 11
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2

print(a)  # h
