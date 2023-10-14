n = int(input())
sigma = 0
m = input().split()
for i in range(n):
    sigma += float(m[i])
print("%.4f" % (sigma / n))