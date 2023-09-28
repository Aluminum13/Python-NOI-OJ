import sys

a = 1
print(type(a))
print(sys.getsizeof(a))

a = 1073741823  # 2^30-1
print(type(a))
print(sys.getsizeof(a))

a = 1073741824  # 2^30
print(type(a))
print(sys.getsizeof(a))

a = 3.14
print(type(a))
print(sys.getsizeof(a))

a = 3.1415926535897932384626433832795028841
print(a)
print(type(a))
print(sys.getsizeof(a))

a = 3.1415926E80 * 3.1415926
print(a)
print(type(a))
print(sys.getsizeof(a))

a = True
print(type(a))
print(sys.getsizeof(a))

a = ""
print(type(a))
print(sys.getsizeof(a))

a = "1"
print(type(a))
print(sys.getsizeof(a))

a = "1234567890"
print(type(a))
print(sys.getsizeof(a))

a = []
print(type(a))
print(sys.getsizeof(a))

a = [1, 2, 3]
print(type(a))
print(sys.getsizeof(a))

a = {}
print(type(a))
print(sys.getsizeof(a))

a = {"a": 1}
print(type(a))
print(sys.getsizeof(a))

a = {1, 2, 3}
print(type(a))
print(sys.getsizeof(a))

"""
出题者是钟爱C/C++的，也不能全怪他，毕竟NOI OJ本质上是为NOI服务的（虽然已经很久不维护了）
NOI是个算法竞赛，谁参加算法竞赛用python啊。
所以事实上本章大部分题目因为都是针对C语言特性量身定做，所以在python这边水土不服.
但是我觉得去思考这些题目的内涵仍然是有价值的。
比如前三道题要求打印类型大小，本意就是希望你了解这些变量占用空间不同，进一步启发你思考他们的存储方式等等。（如果你有兴趣）
这些事情在python中也是能做的。
所以我在这里打印了大部分你可能遇到的类型和空间，如果不感兴趣，可以匆匆看一眼，如果感兴趣，可以去研究一下原因。
不过1.2.1~1.2.3就不用交了。
"""

"""
另外，这道题是第一次需要调用库，大家可以顺便看一看格式
"""