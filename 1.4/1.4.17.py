n = int(input())
if n % 4 + (n % 100 == 0) - (n % 400 == 0):
    print('N')
else:
    print('Y')

"""
如果这道题能看懂做法，那基本上本章毕业了。
"""