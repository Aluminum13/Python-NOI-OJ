print(ord(input()))

"""
这道题本意是想让用C的选手开开眼界（用java也可以）——
强制把字符转换成整型，就可以得到ASCII码，这暗示了其实在C语言中字符型本质上是以ASCII码的方式存储的，
只是当变量被声明为字符型时，会加一层包装，把ASCII码转成对应字符。
但是python这边没有这种震撼，python存储字符型的逻辑是不同的。有兴趣的同学可以自行研究。
"""