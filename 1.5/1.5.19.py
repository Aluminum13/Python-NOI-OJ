n = input()
time = 0
for i in range(n):
  x, y, num_people = input().split()
  time += (x**2 + y**2) / 2500 + num_people * 1.5
if (time/1):
  time += 1
print(int(time))
