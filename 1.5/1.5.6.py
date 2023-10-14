n = int(input())
m = input().split()
m = list(map(int, m))
print(max(m) - min(m))