num = input().split()
print((int(num[0]) + int(num[1])) // int(num[2]))

"""
注意虽然题目中强调了/代表“整除”运算，但那是针对C的。
而在python中就/代表除，//才代表整除。另外%代表取余，或者叫取模运算。
虽然对于非数学且非计算机专业的朋友可能对整除和取模接触不多，但是他们都是计算机科学和数论，组合数学等科目中常用的运算。
"""
