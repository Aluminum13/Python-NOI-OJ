n = int(input())
ang = (n - 2) * 180
m = input().split()
m = list(map(int, m))
print(ang - sum(m))

"""
列表求和也有函数，嘿嘿
"""