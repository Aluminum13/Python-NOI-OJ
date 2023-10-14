m, n = input().split()
m = int(m)
n = int(n)
sigma = 0
for i in range(m + (17 - m % 17) % 17, n + 1, 17):
    sigma += i
print(sigma)

"""
依然是一个值得看懂的range
"""