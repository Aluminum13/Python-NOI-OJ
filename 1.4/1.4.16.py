a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
n = a + b + c
if int(b) > int(a):
    a = b
if int(c) > int(a):
    a = c
if n - a > a:
    print('yes')
else:
    print('no')