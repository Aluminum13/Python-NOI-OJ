import sys

s = input()
if len(s):
    n = ord(s)
else:
    print('NO')
    sys.exit()

if n % 2:
    print('YES')
    sys.exit()
print('NO')

"""
如果你是九分+Runtime Error，并感到百思不得其解，那你来对地方了。
空字符是有ASCII码的（不信可以查表），这道题有一个测试集就是空字符（不打任何东西直接回车），正确输出是NO。
但是如果我们按照上一题的做法，直接n=ord(input())，就出问题了，ord不认空字符。所以我们必须先判断是不是空字符。
顺便，没想到下一道题就体现出了sys.exit对结构的改变。大家可以不用控制语句重写这个程序，看看结构有什么变化。细细体会为什么有时候大家更爱用控制语句。
"""