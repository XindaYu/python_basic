'''
Python3 模块
如果从 Python 解释器退出再进入，那么定义的所有的方法和变量就都消失了。
为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。
模块是一个包含所有定义的函数和变量的文件，其后缀名是.py。
模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
'''
# 导入模块
import support

# 现在可以调用模块里包含的函数了
support.print_func("mukuai")

'''
2.from … import 语句
Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：

from modname import name1[, name2[, ... nameN]]
例如，要导入模块 fibo 的 fib 函数，使用如下语句：

>>> from fibo import fib, fib2
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377
'''

'''
3.from … import * 语句
把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：

from modname import *
这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。
'''

# 4.dir() 函数
# 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
# 如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称:
print(dir(support))

'''
5.从一个包中导入*
如果我们使用 from sound.effects import * 会发生什么呢？
Python 会进入文件系统，找到这个包里面所有的子模块，然后一个一个的把它们都导入进来。
但这个方法在 Windows 平台上工作的就不是非常好，因为 Windows 是一个不区分大小写的系统。
在 Windows 平台平台上，我们无法确定一个叫做 ECHO.py 的文件导入为模块是 echo 还是 Echo，或者是 ECHO
为了解决这个问题，我们只需要提供一个精确包的索引。
导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，
那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。
作为包的作者，可别忘了在更新包之后保证 __all__ 也更新了啊。

以下实例在 file:sounds/effects/__init__.py 中包含如下代码:

__all__ = ["echo", "surround", "reverse"]

这表示当你使用from sound.effects import *这种用法时，你只会导入包里面这三个子模块。
如果 __all__ 真的没有定义，那么使用from sound.effects import *这种语法的时候，
就不会导入包 sound.effects 里的任何子模块。他只是把包sound.effects和它里面定义的所有内容导入进来（可能运行__init__.py里定义的初始化代码）。
这会把 __init__.py 里面定义的所有名字导入进来。并且他不会破坏掉我们在这句话之前导入的所有明确指定的模块。
'''
