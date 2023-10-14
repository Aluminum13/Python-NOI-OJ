a, b, c = input().split()
a = int(a)
b = int(b)
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/' and b:
    print(a // b)
elif c == '/':
    print("Divided by zero!")
else:
    print("Invalid operator!")

"""
如果你只有八分，那可能是因为C语言中两个整数做/运算相当于//，所以其实这边也应该用//
但是用了//也只有9分，暂时不知道为什么。
由于我C语言能做到满分，经过尝试我大概确定了错误的测试集是一个b>0的除法。但我不知道具体错哪了。等待帮助中。
"""