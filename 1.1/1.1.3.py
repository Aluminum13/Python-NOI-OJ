a, b, c = input().split()
output_str = "{:>8} {:>8} {:>8}".format(a, b, c)
print(output_str)

"""
另外一种写法是：
a, b, c = input().split()
print(f"{a:>8} {b:>8} {c:>8}")
"""

"""
还有一种写法是：
num = input().split()
for i in num:
    print(f"{i:>8} ", end="")
我想接着这个例子提一嘴，大家想必发现了，print语句会自动换行，其实是因为print有一个默认参数end="\n"，意味在输出的末尾加一个”换行符“
换句话说，其实你每次输出答案，后面都会跟着一个换行符。但这不影响答案正确。
在这个例子里，end=""，也就是我设置了在末尾加空字符（等于没加），所以换行符没有了。也不影响答案正确。
而且细心的朋友会发现，除此之外，这个写法还理应导致最后有一个多余的空格，但是他也不影响。
什么影响什么不影响呢？为什么呢？这是个有意思的问题，你可以研究，也可以记住常见情况——空格和换行符不影响。
"""

"""
如果你完全理解了以上几个例子的每句话在干什么，你会发现甚至单就这几个例子中出现的元素，结合我们之前提到过的东西，就可以组合出许许多多的做法。
比如如果结合第一种做法的格式和第二种做法的实现逻辑：
a, b, c = input().split()
output_str = f"{a:>8} {b:>8} {c:>8}"
print(output_str)
如果有兴趣和时间，多尝试写几种吧！
"""
