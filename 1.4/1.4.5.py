x, y = input().split()
if int(x) > int(y):
    print('>')
elif int(x) == int(y):
    print('=')
else:
    print('<')