num = input().split()
h = int(num[0])
r = int(num[1])
pi = 3.14159
if 20 * 1E3 % (pi * r ** 2 * h) == 0:
    print(int(20 * 1E3 // (pi * r ** 2 * h)))
else:
    print(int(20 * 1E3 // (pi * r ** 2 * h) + 1))

"""
做测试数据的人是善良的，没有出任何一个刚好整除的情况，所以你直接+1也能满分，但是我们最好还是细心一点。
"""