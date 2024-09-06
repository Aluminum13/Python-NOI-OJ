n = int(input())
time = 0
for i in range(n):
    num = input().split()
    x = float(num[0])
    y = float(num[1])
    num_people = float(num[2])
    time += 2 * (x**2 + y**2)**0.5 / 50 + num_people * 1.5
if (time % 1):
    time += 1
print(int(time))

"""
你知道的，向上取整也可以用math.ceil
"""
