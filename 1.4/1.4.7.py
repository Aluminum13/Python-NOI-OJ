n, m = input().split()
if (int(n) >= 10) + (int(m) >= 20):
    print(1)
else:
    print(0)

"""
这道题的条件写法还有很多，比如：
(int(n) >= 10) or (int(m) >= 20)
(int(n) // 10) + (int(m) // 20)
如果到这里你还不能给出不止一种写法，那么你应该好好回忆一下之前的内容了。
"""