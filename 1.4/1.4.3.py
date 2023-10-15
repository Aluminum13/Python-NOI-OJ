import sys

n = int(input())
if n % 2:
    print('odd')
    sys.exit()
print('even')

"""
这里展示了一点不一样的东西，首先是我在1.2.9里面请求大家别忘了的性质。
你可以这样理解：if本质上只有两种状态 if True 和 if False。如果是前者就执行后面的代码块，如果是后者就不执行
if后面无论跟什么，都是先强行转换成bool型。所以if [表达式] 相当于先 if bool([表达式])，看到底是True还是False。
这样解释是为了让你更好理解，这并不是很精确，但大部分情况下可以这样理解。所以更具体的等你遇到例外再说吧。
所以回忆一下1.2.9，想必你能对这种实现方法有一些理解。
"""
"""
另一个有意思的东西是，除了写else语句，你还可以用控制语句sys.exit（本质上相当于结束程序）来实现一样的效果。
我建议大家不要太轻视这个思想，这不是只用来炫技的做法，我相信以后你们会用到的（虽然可能是以别的形式用到，比如break，continue，pass……）。
"""
"""
我有一些可能和编程不那么紧密相关的肺腑之言想说：
大家可能遇到过一些刚刚入门形式逻辑的魔怔人（只是因为我最近才遇到了这样的人，我向我没有提到的其他学科的魔怔人道歉）
他可能每天会高强度地把真假挂在嘴边——比如他会说：当你抽卡为真的时候，你抽到SSR为真的概率
如果他还习惯用英文，你会听到满嘴的is true，is false。
我认为这是非常好的。

认知科学对儿童语言习得的研究中有提到“快速映射”（fast mapping）和“过度推广”（overextension）现象。
“快速映射”是说儿童在还没有完全理解一个词汇的时候就能够通过上下文提示和联想来进行快速映射，并在对词语含义仍有疑惑的时候就开始积极使用它。
“过度推广”则是说明了儿童在刚学会一个词汇/概念的时候可能会推广到各种不准确的情景。例如学会了词汇“狗”之后，他们可能错误的用它来称呼所有四条腿的动物。

为什么说是儿童语言习得呢，因为研究莫不指出，这些现象有明显的龄段差异，随着年龄增长，这些现象将会消失。

而与此同时，大家也应该听说过一个流传很广的理论——“关键期假说”，就是说人类在幼年时期对学习新语言有独特的优势.
认同这一理论的包括Chomsky在1965年首版的，鼎鼎大名的巨作——在谷歌学术有48000+引用的Aspects of the Theory of Syntax。
还有Lenneberg在1967年发表的The biological foundations of language，奠定关键期假设的核心论文，同样有15000+引用。

说实话，这几乎是不需要证明的事情，人人都在小时候看起来很轻松地掌握了第一语言，而在学习第二语言的过程中却倍感折磨。
我妈肯定没看过这些文章，但她也早在公众号还没有满天飞的年代就虔诚地相信事实肯定如此。

但也有一些文章持有相反的意见，例如SM Ervin-Tripp在1974年发表Is second language learning like the first反驳了这种观点。
例如Stephen Krashen先后发表了一系列关于第二语言习得的论文和著作（真的有一大堆）
他们都通过实验努力地证明，其实第二语言和第一语言没有区别，也没有所谓的“关键期”，随着年龄的增长语言学习能力不但没有下降，反而更上一层楼了。

那到底是什么阻止了我们学习第二语言，或者是什么别的东西？可能正是因为我们不再像小朋友那样还来不及掌握就迫不及待地尝试，甚至不惜闹出各种笑话。
可能是因为作为幼儿的我们正是在大量的输入和反馈中，在一次次的错误使用中，我们得以迅速收敛到一个词真正的含义和适用范围。
但是随着年龄的增长，我们周边的环境，乃至我们自己，都对我们太苛刻了。没有人会耐心地，一次次地纠正我们——取而代之的可能是冷嘲热讽。
我们自己也会难以忍受一直犯错的自己，我们会觉得给别人带来麻烦，感觉自己很丢人，感觉自己令人失望……
”你能不能自己先想，想清楚了再来问“”你能不能少问点这种没价值的问题“”你能不能少犯点这种稍微动点脑就能避免的错“”但凡你学的时候用点心都不会这个时候来问这个“
我想这说不定是人不得不承受的痛苦。我也不过是一边同情着别人，一边每天都在给别人施加这样的压力。For shame！For shame！
但是还好编译器，OJ不会嘲笑我们。虽然他们也不会纠正我们，但是他们真的只是轻描淡写地告诉我们我们错了，仅此而已。
就算是再幼稚，再不值得犯的错误也不会引起一丝额外的语气。
所以我真的希望趁此机会，在屏幕面前，我们也能久违的对自己更宽容一些。像一个儿童一样去积极地快速映射，去过度推广。
积极地在每个觉得可能能用的地方去试着用，哪怕会不合时宜，把简单易读的程序变得又臭又长，哪怕会犯错。
就像我们现在正在探索能不能把一个普通的表达式当作布尔表达式用一样。
你还可以去探索所有其他的东西能不能当条件，当然你会经常”过度推广“了，但是没关系，只有编译器知道。
作为一个例子：比如你可以尝试拿赋值语句a=b当条件——Python不行，但是有的语言真的可以。
但是Python3.8之后的版本引入了海象运算符，a:=b，它也有赋值功能，而且真可以当条件。
如果你真的试了一下if a=b，而且用的是pycharm，他甚至会在错误报告里问你是不是想用==或者:=。

希望你能做回那个充满兴趣，又充满自信的孩子。希望我，其他人，可能还有你自己，会支持你。
"""