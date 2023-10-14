m, n = input().split()
m = int(m)
n = int(n)
sigma = 0
for i in range(m + 1 - m % 2, n + 1, 2):
    sigma += i
print(sigma)

"""
range里面的部分是值得细品一下的
"""