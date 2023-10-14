a, b, c = input().split()
if int(b) > int(a):
    a = b
if int(c) > int(a):
    print(c)
else:
    print(a)