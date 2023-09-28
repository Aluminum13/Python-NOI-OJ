x1, y1, x2, y2, x3, y3 = input().split()
a = ((float(x1) - float(x2)) ** 2 + (float(y1) - float(y2)) ** 2) ** 0.5
b = ((float(x1) - float(x3)) ** 2 + (float(y1) - float(y3)) ** 2) ** 0.5
c = ((float(x2) - float(x3)) ** 2 + (float(y2) - float(y3)) ** 2) ** 0.5
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(f"{s:.2f}")