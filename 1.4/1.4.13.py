x = float(input())
if x < 5:
    print("%.3f" % (2.5 - x))
elif x < 10:
    print("%.3f" % (2 - 1.5 * (x - 3) ** 2))
else:
    print("%.3f" % (x / 2 - 1.5))