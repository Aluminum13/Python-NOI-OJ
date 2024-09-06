import sys


def matrix_multiply(A, B):
    # 定义2*2矩阵乘法
    return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]


def matrix_power(A, n):
    # 快速幂算法
    if n == 1:
        return A
    if n % 2:
        half_pow = matrix_power(A, n // 2)
        return matrix_multiply(matrix_multiply(half_pow, half_pow), A)
    else:
        half_pow = matrix_power(A, n // 2)
        return matrix_multiply(half_pow, half_pow)


n = int(input())
A = [[1, 1], [1, 0]]
if n == 1:
    print(1)
    sys.exit()
fibonacci = matrix_power(A, n - 1)
print(fibonacci[0][0])

"""
第三个算法利用到了一些数学知识，如果对线性代数很不熟悉的朋友可以考虑试着边查边看懂他。（这应该是一个非常经典的例题，全网到处都有讲解。）
当然不看懂也完全没关系。看个云里雾里不要紧。但是粗浅地看一看，有点感觉也好。因为这里面的思路比具体计算要重要得多。而思路其实没有那么难懂。
还记得在1.5.17-2我们说快速幂的时间复杂度是log2(n)吗
那有没有一种可能，递推运算可以视为一个幂运算呢？
熟悉的朋友可能已经知道我在说什么了——是的，你可以把递推算符化。
对不熟悉的朋友我多解释几句。如果你是数学系的，你肯定不需要看这一段。如果你不是数学系，那好，我可以打包票你这辈子处理的绝大多数代数问题都定义在线性空间上。
说绝大多数是保守了，起码99.99%。所以你只需要知道，我接下来介绍的性质适用于你处理的任何问题就行。（等遇到不适用的再说）
线性空间有一些非常好的性质。其中就包括，任何“操作”都可以抽象为左乘一个算符（记住是乘在左边，因为很可惜我们接下来要介绍的东西不保证交换律，乘在左还是右是不同的）
如果对a做b操作，则必有一个算符c，可以使得c*a等价于对a做b操作。
我们注意到每做一次操作相当于左乘一个c
那做n次操作，就相当于c^n*a。
递推是一个操作，所以肯定能够构造一个算符，让递推n次等价于对这个算符做n次幂。也就是一定存在一个和快速幂复杂度一致的，log2(n)算法。
这里补充一下——还要乘以算符自带的复杂度，但是线性递推的复杂度是O(1)。
你想一下你用循环做一次递推，复杂度不就是O(1)吗，说明这个操作就这么简单，你换一个其他的等价运算也没道理会复杂很多。
上面讲的那些就是完整思想，网上大部分地方都不会写清楚，只是莫名其妙就说用矩阵乘法可以优化。所以我额外多解释了几句。
而接下来我们就只需要找这个算符是什么，是一个纯粹的技术问题了，而且到处都能搜到，所以我们把过程写得简略一点。
|1 1|| F(n) |   |F(n+1)|    | F(n) |
|1 0||F(n-1)| = | F(n) | = A|F(n-1)|
受限于格式，写的挺不好看，我建议大家还是去网上搜一张好点的图来看。
按照矩阵乘法规则，上式的左边等式显然成立。搜一下矩阵乘法的定义，这一步很容易验证（真的很容易，你要不试一下）
而对于右边的等式，此处A就是我们说的那个抽象的算符，它的定义就是当他作用于列向量(F(n);F(n-1))时，能够得到(F(n+1);F(n))。所以没什么理由，这是定义。
那我们通过这个等式关系就找到了A算符的具体形式，就是最左边那个（1 1；1 0）的矩阵。
那么按照我们之前总结的，线性空间的性质，既然A是递推一位，那么应该有：
| F(n) |          |F(1)|          |1|       |1 1|
|F(n-1)| = A^(n-1)|F(0)| = A^(n-1)|0|，其中A=|1 0|
又代入矩阵乘法的规则可以轻松得到，F(n)=A^(n-1)[1][1]（即A^(n-1)也为一个2*2的矩阵，他的左上即为F(n)）
接下来就只剩下计算A^(n-1)了。这个程序就是在具体实现这个计算流程。
"""
"""
这个程序的实现不必全部看懂。快速幂部分实际上用了递归（函数自我调用）实现，这是稍微高级一点的算法了。新手入门暂且不用管那么多。
但是我可以稍微解释一下快速幂算法的原理（不难，真的）。
简单来说就是，a^n，当n为偶数可以拆成a^(n//2)^2，n为奇数则可以拆成a^(n//2)^2 * a
这样依次拆分，可以拆成log2(n)的整数部分层，每层只需要做一次平方操作（相当于一次乘法），如果是奇数需要再加一次乘法
也就是说计算量<=2 * int(log2(n)) <= 2 * log2(n)，是log2(n)数量级
举例，如果是2的9次方：
9
4(1)
2
1
我们其实需要做的是：(2^1)^2 = 2^2, (2^2)^2 = 2^4, (2^4)^2 * 2^1 = 2^9
在这个例子中，我们其实制作了三次平方（相当于三个乘法）+一个作为余数的乘法
其实在知道这一点以后，程序也没有那么难看懂了，如果不甘心可以再看两眼？
这个算法的时间复杂度也是O(log2(n))，空间复杂度也是O(1)（和通项公式法一致）
"""
