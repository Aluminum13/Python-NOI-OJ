a = input().split()
b = input().split()
x = float(a[0]) - float(b[0])
y = float(a[1]) - float(b[1])
print(f"{(x**2 + y**2)**0.5:.3f}")

"""
你当然还可以用内置库math里面的math.sqrt()来实现开根号。math.pow()来实现幂运算，还有其他更多实现方式
这里用**主要是考虑到，这是可能更符合大家日常数学书写习惯的方法。
"""
