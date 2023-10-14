num = input().split()
n = int(num[0])
x = int(num[1])
y = int(num[2])
if y % x == 0:
    print(max(0, n - y // x))
else:
    print(max(0, n - y // x - 1))

"""
虽然超纲用了if，但是更可怕的是
我居然想不到不用if怎么做（
如果有人不用if做出来了请告诉我！
"""
