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
再通过break在适当的时候跳出。
"""

"""
2.
n = int(input())
iterations = [n]

for i in iterations:
    if i == 1:
        break
    if i % 2:
        next_value = i * 3 + 1
        print("%d*3+1=%d" % (i, next_value))
    else:
        next_value = i // 2
        print("%d/2=%d" % (i, next_value))
    iterations.append(next_value)

print("End")
这个方案和1.5.7的思路基本一致，只是换了一种写法。
在循环过程中动态修改list来实现基于for的不定长循环。
"""

"""
def collatz(n):
    if n == 1:
        print("End")
        return
    if n % 2:
        print(f"{n}*3+1={n * 3 + 1}")
        collatz(n * 3 + 1)
    else:
        print(f"{n}/2={n // 2}")
        collatz(n // 2)

n = int(input())
collatz(n)
这是相对比较进阶的做法，利用了递归来模拟不定长的循环迭代。
我们之前也曾经介绍过递归的概念（在介绍快速幂算法的时候），这里也一样，定义了一个collatz函数，并在其中不停的调用自身来实现迭代。
"""
