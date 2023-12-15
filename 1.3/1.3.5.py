num = input().split()
print(f"{float(num[0]) / float(num[1]):.9f}")

"""
或者学过C语言的朋友可能会更熟悉另一种写法
print("%.9f" % (float(num[0]) / float(num[1])))
"""
