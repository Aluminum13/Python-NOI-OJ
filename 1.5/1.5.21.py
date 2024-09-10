n = int(input())

while n!=1:
    if n % 2:
        print("%d*3+1=%d" % (n, n := n * 3 + 1))
    else:
        print("%d/2=%d" % (n, n := n // 2))

print("End")

"""
这是1.5第一道为while量身打造的题目，因为他有一个需要动态判断的截止条件，同时没有确定的循环长度。
并且我们通过海象运算符把格式写得更清爽了。
但是我们之前就提到过，for循环可以解决所有的循环问题，也写出不定长的循环。
我们之前就在1.5.7给大家打过一个样。
那还有没有更多的写法呢？
这里再提供三种实现思路：
"""

"""
1.
import itertools

n = int(input())

for _ in itertools.count():
    if n == 1:
        break
    if n % 2:
        print("%d*3+1=%d" % (n, n := n * 3 + 1))
    else:
        print("%d/2=%d" % (n, n := n // 2))

print("End")
这个方案利用python自带的标准库itertools中的count函数自动生成一个无限的数字序列，实现无限长循环。
之后再通过break命令在适当的时候跳出。
"""
