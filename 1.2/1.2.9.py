print(int(bool(int(input()))))

"""
这是一个python也有的特性，非0/非空字符对应bool型中的True，而0/空字符则对应bool型中的False。
而bool型中的True是用1储存的，Flase则是0。
这可能有点拗口，不过大家可以自己试试就理解了：
print(bool(0))
print(bool(''))
print(bool(int(114)))
print(bool(float(5.14)))
print(bool('1919'))
print(int(False))
print(int(True))
print(float(False))
print(float(True))
需要注意的是，尽管如此，False和True强制转换成str的时候，行为会不一样，大家可以试试
print(str(False))
print(str(True))
这个特性很有意思，以后我用到的时候希望读者不要已经忘了。
"""
