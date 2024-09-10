n = int(input())

while n!=1:
    if n % 2:
        print("%d*3+1=%d" % (n, n := n * 3 + 1))
    else:
        print("%d/2=%d" % (n, n := n // 2))

print("End")

"""
总之通过海象运算符和while循环把格式写得更清爽了。
但是它能不能通过for循环实现呢？肯定是可以的，大家可以自行思考。
我可以提供一个最基本的思路：
"""
