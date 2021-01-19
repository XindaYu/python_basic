# Python中单行注释以 # 开头
# 多行注释可以用多个 # 号，还有 ''' 和 """

# -------------------------------------------------------------------------------
# 1...行和缩进:用缩进来写模块
#        缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。
# --IndentationError: unindent does not match any outer indentation level
# --错误表明，你使用的缩进方式不一致，有的是 tab 键缩进，有的是空格缩进，改为一致即可
# 建议你在每个缩进层次使用 单个制表符 或 两个空格 或 四个空格 , 切记不能混用
'''
if True:
    print("Answer")
else:
    print("True")
'''

# 没有严格缩进，在执行时会报错
#  print ("False")

# -------------------------------------------------------------------------------
# 2...多行语句:Python语句中一般以新行作为语句的结束符。
# 但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示
'''
total = item_one + \
        item_two + \
        item_three
'''

# 语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：
'''
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
'''
# -------------------------------------------------------------------------------
# 3...数字(Number)类型
#  int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
#  bool (布尔), 如 True。
#  float (浮点数), 如 1.23、3E-2
#  complex (复数), 如 1 + 2j、 1.1 + 2.2j

# -------------------------------------------------------------------------------
# 4...字符串(String)
'''
    python中单引号和双引号使用完全相同。
    使用三个引号('or")可以指定一个多行字符串。
    转义符 '\'
    反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 
        r"this is a line with \n" 则\n会显示，并不是换行。
    按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
    字符串可以用 + 运算符连接在一起，用 * 运算符重复。
    Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
    Python中的字符串不能改变。
    Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
    字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
'''

word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

str = '012345'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符，到冒号右边的那个数之前，左闭右开
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔两个的字符（就是两个数中间夹着一个）
print('------------------------------')
print(str[1::2])  # 输出从第二个开始到最后且每隔两个的字符（就是两个数中间夹着一个）
print(str[1::2] * 2)  # 输出从第二个开始到最后且每隔两个的字符（就是两个数中间夹着一个）
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nruntest')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nruntest')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义（raw string）自然状态的

# -------------------------------------------------------------------------------
# 5...空行
# 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。
# 类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
# 空行与代码缩进不同，空行并不是Python语法的一部分。
# 书写时不插入空行，Python解释器运行也不会出错。
# 但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
# 记住：空行也是程序代码的一部分。

# -------------------------------------------------------------------------------
# 6...同一行显示多条语句
# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
import sys;

x = 'test';
sys.stdout.write(x + '\n')

# -------------------------------------------------------------------------------
# 7...多个语句构成代码组
# 缩进相同的一组语句构成一个代码块，我们称之代码组。
# 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，
# 该行之后的一行或多行代码构成代码组。
# 我们将首行及后面的代码组称为一个子句(clause)。
'''
if expression : 
   suite
elif expression : 
   suite 
else : 
   suite
'''

# -------------------------------------------------------------------------------
# 8...print 输出
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()  # 输出a b

# -------------------------------------------------------------------------------
# 9...import 与 from...import
'''
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''
# 导入 sys 模块
import sys

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

# 导入 sys 模块的 argv,path 成员
from sys import path  # 导入特定的成员

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path
