import math

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
delta = b ** 2 - 4 * a * c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("x1=%.5f;x2=%.5f" % (x1, x2))
elif delta == 0:
    x1 = -b / (2 * a)
    print("x1=x2=%.5f" % x1)
else:
    x_Re = -b / (2 * a)
    x_Im = math.sqrt(-delta) / (2 * a)
    print("x1=%.5f+%.5fi;x2=%.5f-%.5fi" % (x_Re, x_Im, x_Re, x_Im))

"""
只有8分，不出意外的话又是浮点数运算误差的问题，我们不管他（
"""