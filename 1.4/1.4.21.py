num = input().split()
n = int(num[0])
x = int(num[1])
y = int(num[2])
if y % x == 0:
    print(max(0, n - y // x))
else:
    print(max(0, n - y // x - 1))