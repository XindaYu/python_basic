# -------------------------------------------------------------------
# Python数据类型转换
# 我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
# 以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值
# ····················int(x [,base])····················
# 将x转换为一个整数
print(int(3.6))  # 3
print(int('12', 16))  # 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制 18
# print("str",2) 报错，str都是整数10进制

# ····················float()
# float() 函数用于将整数和字符串转换成浮点数。
print(float(112))  # 112.0
print(float('123'))  # 字符串->123.0

# ····················complex()
# complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。
# 如果第一个参数为字符串，则不需要指定第二个参数
print(complex(1, 2))  # (1+2j)
print(complex(1))  # (1+0j)
print(complex("1"))  # 当做字符串处理(1+0j)
print(complex("1+2j"))  # 这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错

# ····················str()
# str() 函数将对象转化为适于人阅读的形式。 class str(object='')
print(str(123))
dict3 = {'runoob': 'run', 'google': 'google.com'}
print(str(dict3))  # {'run': 'runoob.com', 'google': 'google.com'}

# ····················repr() 函数
# repr() 函数将对象转化为供解释器读取的形式。返回一个对象的 string 格式。
s = 'RUN'
print(repr(s))  # 'RUN'

# ····················eval() 函数
# eval() 函数用来执行一个字符串表达式，并返回表达式的值。返回表达式计算结果。
# eval(expression, globals, locals)
# expression -- 表达式。
# globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
# locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
x = 7
print(eval('3 * x'))  # 21
print(eval('pow(2,2)'))  # 4
n = 5
print(eval("n + 4"))  # 9

# ···················· tuple 函数
# tuple 函数将可迭代系列（如列表）转换为元组。
list1 = ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1 = tuple(list1)
print(tuple1)  # ('Google', 'Taobao', 'Runoob', 'Baidu')

# ····················List list()方法
# list() 方法用于将元组或字符串转换为列表。
# 注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
aTuple = (123, 'Google', 'Runoob', 'Taobao')
list1 = list(aTuple)
print("列表元素 : ", list1)  # 列表元素 :  [123, 'Google', 'Runoob', 'Taobao']

str = "Hello World"
list2 = list(str)
print("列表元素 : ", list2)  # 列表元素 :  ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

# ····················set() 函数
# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
x = set('mno')
y = set('opqr')
print(x, y)  # {'n', 'o', 'm'} {'r', 'o', 'q', 'p'}
print(x & y)  # {'o'}
print(x | y)  # {'r', 'q', 'm', 'o', 'p', 'n'}
print(x - y)  # {'n', 'm'}

# ····················dict() 函数
# dict() 函数用于创建一个字典
# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)
# **kwargs -- 关键字  mapping -- 元素的容器  iterable -- 可迭代对象

'''
>>>dict()                        # 创建空字典
{}
>>> dict(a='a', b='b', t='t')     # 传入关键字
{'a': 'a', 'b': 'b', 't': 't'}
>>> dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
{'three': 3, 'two': 2, 'one': 1} 
>>> dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典
{'three': 3, 'two': 2, 'one': 1}
>>>
'''
# ····················frozenset() 函数
# frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
# iterable -- 可迭代的对象，比如列表、字典、元组等等。
# 返回新的 frozenset 对象，如果不提供任何参数，默认会生成空集合。

a = frozenset(range(10))  # 生成一个新的不可变集合
print(a)
b = frozenset('runoob')
print(b)

# ····················chr() 函数
# chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
# chr(i)i -- 可以是10进制也可以是16进制的形式的数字,返回值是当前整数对应的 ASCII 字符。

print(chr(0x30), chr(0x31), chr(0x61))  # 十六进制0 1 a
print(chr(48), chr(49), chr(97))  # 十进制0 1 a

# ····················ord() 函数
# ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
# 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
# 如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常
print(ord('a'))  # 97
print(ord('b'))  # 98

# ····················hex() 函数
# hex() 函数用于将10进制整数转换成16进制，以字符串形式表示。
# hex(x)  x -- 10进制整数
print(hex(255))  # 0xff
print(hex(-42))  # -0x2a
print(type(hex(12)))  # <class 'str'>

# ····················oct() 函数
# oct() 函数将一个整数转换成 8 进制字符串。
# Python2.x 版本的 8 进制以 0 作为前缀表示。
# Python3.x 版本的 8 进制以 0o 作为前缀表示。
# oct(x)  x是整数
print(oct(10)) #0o12
