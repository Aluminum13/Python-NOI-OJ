import sys

n, k = input().split()
n = int(n)
k = int(k)
money = n
price = 200
for i in range(19):
    if money >= price:
        print(i + 1)
        sys.exit()
    money += n
    price *= 1 + k * 0.01
print('Impossible')
