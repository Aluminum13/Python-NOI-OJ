n = int(input())
b = True
for i in [3, 5, 7]:
    if not n % i:
        print(i, end=' ')
        b = False
if b:
    print('n')

"""
依然是朝纲使用了for语句，但是我想这应该不难看懂。
另外用b作为一个指示器，这也是灵活使用可以优化结构的小技巧。
"""