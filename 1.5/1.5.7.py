n = int(input())
list1 = [1]
gold, silver, copper = 0, 0, 0
for i in list1:
    if i < n:
        list1 += [i + 1]
    medal = input().split()
    gold += int(medal[0])
    silver += int(medal[1])
    copper += int(medal[2])
print(gold, silver, copper, gold + silver + copper)

"""
还记得我在1.5.4问你们while和for的优缺点吗？
我知道有人会觉得，噢，for循环必须一开始就定死迭代的范围，while则可以不定长循环。甚至很多不负责任的搜索结果都会这么告诉你。
因此在这里我想告诉你——不全对，for循环也可以实现不定长，也可以在循环中调整迭代范围。
本题只是一个最简单的例子，你事实上可以利用这种思路做到更多，这个例子只是为了告诉你可以这样做，绝不代表它只能这样做。
当然在本题中，这个技巧多此一举。甚至在你未来的生涯中你都不一定会遇到要用这个技巧的时候。
但至少它很有意思，不是吗，知道能这么写很有意思。
"""