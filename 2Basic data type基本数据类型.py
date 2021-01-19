# --------------------------------------------------------------
# 1...变量
# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
# 等号（=）用来给变量赋值。
# 等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "test"  # 字符串

print(counter)
print(miles)
print(name)

# 多个变量赋值
a = b = c = 1
a1, b1, c1 = 1, 2, "a"
print(c1)

# -------------------------------------------------------------------
# 2...标准数据类型
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Set（集合）
# Dictionary（字典）
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

# -------------------------------------------------------------------
# 2.1...Number（数字）
# Python3 支持 int、float、bool、complex（复数）。
# 在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# 像大多数语言一样，数值类型的赋值和计算都是很直观的。
# 内置的 type() 函数可以用来查询变量所指的对象类型。
print('2.1number---------------------')
a2, b2, c2, d2 = 20, 5.5, True, 4 + 3j
print(type(a2), type(b2), type(c2), type(d2))
print(isinstance(a2, int))
# 当指定一个值时，Number 对象就会被创建：
var1 = 1
var2 = 10
var3 = 100
print(var1)
# 可以使用del语句删除一些对象引用
del var1
print("删除后")
# print(var1) # 出错Traceback (most recent call last)
print(5 + 4)  # 加法
print(4.3 - 2)  # 减法
print(3 * 7)  # 乘法
print(2 / 4)  # 除法，得到一个浮点数  ->0.5
print(2 // 4)  # 除法，得到一个整数，数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数->0
print(17 % 3)  # 取余->2
print(2 ** 5)  # 乘方->32
# 在混合计算时，Python会把整型转换成为浮点数。
print(3 * 3.75 / 1.5)  # ->7.5
# 在交互模式中,最后被输出的表达式结果被赋值给变量 _
'''
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
# _ 变量应被用户视为只读变量
'''

# -------------------------------------------------------------------
# 2.2...String（字符串）
# Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。
# 字符串的截取:变量[头下标:尾下标]
strs = '012345'

print(strs)  # 输出字符串012345
print(strs[0:-1])  # 输出第一个到倒数第二个的所有字符01234
print(strs[0])  # 输出字符串第一个字符0
print(strs[2:5])  # 输出从第三个开始到第五个的字符234
print(strs[2:])  # 输出从第三个开始的后的所有字符2345
print(strs * 2)  # 输出字符串两次，也可以写成 print (2 * str)012345012345
print(strs + "TEST")  # 连接字符串012345TEST

print('012\n345')  # 一行012一行345
print(r'012\n345')  # 可以在字符串前面添加一个 r，表示原始字符串：012\n345
# 反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行。
word = 'Python'
print(word[0], word[5])  # P n
print(word[-1], word[-6])  # n P
# Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。
word = 'aaa'
print(word)

# -------------------------------------------------------------------
# 2.3List（列表）
# 列表可以完成大多数集合类的数据结构实现。
# 列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套)
# 列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
# 列表截取的语法格式如下：变量[头下标:尾下标] 索引值以 0 为开始值，-1 为从末尾的开始位置。
list2 = ['abcd', 123, 1.23, 'test', 45.6]
tinylist = [123, 'runtest']

print(list2)  # 输出完整列表['abcd', 123, 1.23, 'test', 45.6]
print(list2[0])  # 输出列表第一个元素abcd
print(list2[1:3])  # 从第二个开始输出到第三个元素[123, 1.23]
print(list2[2:])  # 输出从第三个元素开始的所有元素[1.23, 'test', 45.6]
print(tinylist * 2)  # 输出两次列表
print(list2 + tinylist)  # 连接列表['abcd', 123, 1.23, 'test', 45.6, 123, 'runtest']

# 列表中的元素是可以改变的
a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
print(a)  # [9, 2, 13, 14, 15, 6]
a[2:5] = []  # 将对应的元素值设置为 []
print(a)  # [9, 2, 6]

# Python 列表截取可以接收第三个参数，参数作用是截取的步长，
# 以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
test = [1, 2, 3, 4, 5, 6]
print(test[1::2])  # [2, 4, 6]

# 如果第三个参数为负数表示逆向读取，以下实例用于翻转字符串：
# 通过空格将字符串分隔符，把各个单词分隔为列表
input = 'I like english'
inputWords = input.split(" ")

# 翻转字符串
# 假设列表 list = [1,2,3,4],
# list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
# inputWords[-1::-1] 有三个参数
# 第一个参数 -1 表示最后一个元素
# 第二个参数为空，表示移动到列表末尾
# 第三个参数为步长，-1 表示逆向
inputWords = inputWords[-1::-1]

# 重新组合字符串
output = ' '.join(inputWords)
print(output)  # english like I

# -------------------------------------------------------------------
# 2.4Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
# 元组中的元素类型也可以不相同：

tuple2 = ('abcd', 786, 2.23, 'runtest', 70.2)
tinytuple = (123, 'runtest')

print(tuple2)  # 输出完整元组('abcd', 786, 2.23, 'runtest', 70.2)
print(tuple2[0])  # 输出元组的第一个元素abcd
print(tuple2[1:3])  # 输出从第二个元素开始到第三个元素(786, 2.23)
print(tuple2[2:])  # 输出从第三个元素开始的所有元素(2.23, 'runtest', 70.2)
print(tinytuple * 2)  # 输出两次元组(123, 'runtest', 123, 'runtest')
print(tuple2 + tinytuple)  # 连接元组('abcd', 786, 2.23, 'runtest', 70.2, 123, 'runtest')
# tuple[0]=1    -># 修改元组元素的操作是非法的

# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号

# -------------------------------------------------------------------
# 2.5Set（集合）
# 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# 创建格式：1:  setname = {value01,value02,...}或者2:  set(value)
sites = {'Google', 'Taobao', 'Run', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Run' in sites:
    print('Run 在集合中')
else:
    print('Run 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)  # {'b', 'r', 'c', 'd', 'a'}
print(b)  # {'c', 'l', 'z', 'm', 'a'}
print(a - b)  # a 和 b 的差集{'b', 'r', 'd'}
print(a | b)  # a 和 b 的并集{'r', 'l', 'm', 'z', 'b', 'c', 'a', 'd'}
print(a & b)  # a 和 b 的交集{'a', 'c'}
print(a ^ b)  # a 和 b 中不同时存在的元素{'b', 'r', 'l', 'm', 'd', 'z'}

# -------------------------------------------------------------------
# 2.6Dictionary（字典）
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
# 键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。

dict = {}
dict['one'] = "1 - aaa"
dict[2] = "2 - bbb"

tinydict = {'name': 'runtest', 'code': 1, 'site': 'www.baidu.com'}

print(dict['one'])  # 输出键为 'one' 的值 1 - aaa
print(dict[2])  # 输出键为 2 的值 2 - bbb
print(tinydict)  # 输出完整的字典 {'name': 'runtest', 'code': 1, 'site': 'www.baidu.com'}
print(tinydict.keys())  # 输出所有键 dict_keys(['name', 'code', 'site'])
print(tinydict.values())  # 输出所有值 dict_values(['runtest', 1, 'www.baidu.com'])

'''
# 构造函数 dict() 可以直接从键值对序列中构建字典如下：
>>> dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
>>> dict(Runoob=1, Google=2, Taobao=3)
{'Runoob': 1, 'Google': 2, 'Taobao': 3}
>>>
'''
# 字典类型也有一些内置的函数，例如clear()、keys()、values()等。
