# String（字符串）
# Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。
# 字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。
# -----创建字符串-----很简单，只要为变量分配一个值即可。例如：
strs = '012345'
var1 = 'Hello World!'
var2 = "Runtest"

# Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
# Python 访问子字符串，可以使用方括号 [] 来截取字符串，字符串的截取的语法格式如下：
# -----字符串的截取-----:变量[头下标:尾下标],索引值以 0 为开始值，-1 为从末尾的开始位置
print(strs)  # 输出字符串012345
print(strs[:])  # 输出完整字符串
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

# -----Python 字符串更新-----
# 你可以截取字符串的一部分并与其他字段拼接
var1 = 'Hello World!'
print("已更新字符串 : ", var1[:6] + 'new!')

# ------------------------------Python转义字符------------------------------
# python 用反斜杠 \ 转义字符
# \(在行尾时),续行符
print("line1 \
... line2 \
... line3")  # line1 ... line2 ... line3

# \\	反斜杠符号
print("\\")  # \

# \'	单引号
print('\'')  # '

# \"	双引号
print("\"")  # "

# \b	退格(Backspace)
print("Hello \b World!")  # Hello World!

# \000	空
print("\000")
# \v	纵向制表符
print("Hello \v World!")
# \t	横向制表符
print("Hello \t World!")
# \r	回车，将 \r 后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成。
print('google runoob taobao\r123456')
print(r'012\n345')  # 可以在字符串前面添加一个 r，表示原始字符串：012\n345
# \yyy	八进制数，y 代表 0~7 的字符，例如：\012 代表换行。
print("\110\145\154\154\157\40\127\157\162\154\144\41")
# \xyy	十六进制数，以 \x 开头，y 代表的字符，例如：\x0a 代表换行
print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")

# -----------------------------Python字符串运算符-----------------------------
# 下表实例变量 a 值为字符串 "Hello"，b 变量值为 "Python"：
# +	字符串连接	a + b 输出结果： HelloPython
# *	重复输出字符串	a*2 输出结果：HelloHello
# []	通过索引获取字符串中字符	a[1] 输出结果 e
# [ : ]	截取字符串中的一部分，遵循左闭右开原则，str[0:2] 是不包含第 3 个字符的。	a[1:4] 输出结果 ell
# in	成员运算符 - 如果字符串中包含给定的字符返回 True	'H' in a 输出结果 True
# not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	'M' not in a 输出结果 True
# r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。
#       原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if ("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')

# -----------------------------Python字符串格式化-----------------------------
# Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，
# 但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
print("我叫 %s 今年 %d 岁!" % ('小明', 10))
# python 字符串格式化符号:
#      %c	 格式化字符及其ASCII码
#      %s	 格式化字符串
#      %d	 格式化整数
#      %u	 格式化 无符号 整型
#      %o	 格式化无符号 八进制数
#      %x	 格式化无符号 十六进制数
#      %X	 格式化无符号 十六进制数（大写）
#      %f	 格式化 浮点数字，可指定小数点后的精度
#      %e	 用科学计数法格式化浮点数
#      %E	 作用同%e，用科学计数法格式化浮点数
#      %g	 %f和%e的简写
#      %G	 %F 和 %E 的简写
#      %p	 用十六进制数格式化变量的地址
#
# 格式化操作符辅助指令
# *	定义宽度或者小数点精度
# -	用做左对齐
# +	在正数前面显示加号( + )
# <sp>	在正数前面显示空格
# #	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
# 0	显示的数字前面填充'0'而不是默认的空格
# %	'%%'输出一个单一的'%'
# (var)	映射变量(字典参数)
# m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
#
# ：：：：：：->format 格式化函数
# Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
# 基本语法是通过 {} 和 : 来代替以前的 % 。
# format 函数可以接受不限个参数，位置可以不按顺序。
# ....不设置参数
print("{} {}".format("hello", "world"))  # 不设置指定位置，按默认顺序 ->:hello world
print("{0} {1}".format("hello", "world"))  # 设置指定位置
print("{0} bc {0} {1}".format("hello", "world"))  # 设置指定位置

# ...设置参数
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "百度", "url": "www.baidu.com"}
print("网站名：{name}, 地址 {url}".format(**site))  # 要加**

# 通过列表索引设置参数
my_list = ['百度', 'www.baidu.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的


# 也可以向 str.format() 传入对象：
class AssignValue(object):
    def __init__(self, value):
        self.value = value


my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的

# ---------------------------------数字格式化--------------------------
# str.format() 格式化数字的多种方法：
# 3.1415926	{:.2f}	3.14	保留小数点后两位
# 3.1415926	{:+.2f}	+3.14	带符号保留小数点后两位
# -1	{:+.2f}	-1.00	带符号保留小数点后两位
# 2.71828	{:.0f}	3	不带小数

# 5	{:0>2d}	05	数字补零 (填充左边, 宽度为2)
# 5	{:x<4d}	5xxx	数字补x (填充右边, 宽度为4)
# 10	{:x<4d}	10xx	数字补x (填充右边, 宽度为4)
# 1000000	{:,}	1,000,000	以逗号分隔的数字格式

# 0.25	{:.2%}	25.00%	百分比格式
# 1000000000	{:.2e}	1.00e+09	指数记法
# 13	{:>10d}	->:        13	 右对齐 (默认, 宽度为10)
# 13	{:<10d}	->:13	         左对齐 (宽度为10)
# 13	{:^10d}	->:    13	     中间对齐 (宽度为10)

# ^, <, > 分别是居中、左对齐、右对齐，后面带宽度，
# : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
# + 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格
# b、d、o、x 分别是二进制、十进制、八进制、十六进制。
# 此外我们可以使用大括号 {} 来转义大括号，如下实例：
print("{} 对应的位置是 {{0}}".format("runtest"))  # runtest 对应的位置是 {0}
print("{:.2f}".format(3.1415926))
'''
进制
'{:b}'.format(11)    1011
'{:d}'.format(11)    11
'{:o}'.format(11)    13
'{:x}'.format(11)    b
'{:#x}'.format(11)   0xb
'{:#X}'.format(11)	 0XB
'''

# --------------------------------------Python 三引号----------------------------
# Python 中三引号可以将复杂的字符串进行赋值。
# Python 三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
# 三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）。
hi = '''hi 
there'''
print(hi)

# 三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。
# 一个典型的用例是，当你需要一块HTML或者SQL时，这时当用三引号标记，使用传统的转义字符体系将十分费神。
# errHTML = '''
# <HTML><HEAD><TITLE>
# Friends CGI Demo</TITLE></HEAD>
# <BODY><H3>ERROR</H3>
# <B>%s</B><P>
# <FORM><INPUT TYPE=button VALUE=Back
# ONCLICK="window.history.back()"></FORM>
# </BODY></HTML>
# '''

# cursor.execute('''
# CREATE TABLE users (
# login VARCHAR(8),
# uid INTEGER,
# prid INTEGER)
# ''')

# -------------------Unicode 字符串-----------------
# Python 中定义一个 Unicode 字符串和定义一个普通字符串一样简单
# >>>u'Hello World !'
# 'Hello World !'
# 引号前小写的"u"表示这里创建的是一个 Unicode 字符串。
# 如果你想加入一个特殊字符，可以使用 Python 的 Unicode-Escape 编码。如下例所示：
# >>> u'Hello\u0020World !'
# 被替换的 \u0020 标识表示在给定位置插入编码值为 0x0020 的 Unicode 字符（空格符）


# -------------------------------------------python的字符串内建函数
# 字符串方法是从python1.6到2.0慢慢加进来的——它们也被加到了Jython中。
# 这些方法实现了string模块的大部分方法，如下表所示列出了目前字符串内建支持的方法，所有的方法都包含了对Unicode的支持，有一些甚至是专门用于Unicode的。

# ------------count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
# https://www.runoob.com/python/python-strings.html
str = "this is string example....wow!!!";
print(str.count('i', 4, 40))  # 2
print(str.count('i', 4))  # 2
print(str.count('i'))  # 3

# -----------index()方法
# index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，
# 则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
# index()方法语法：
#   str.index(str, beg=0, end=len(string))
#   str -- 指定检索的字符串；beg -- 开始索引，默认为0；end -- 结束索引，默认为字符串的长度。
str1 = "Runtext example....wow!!!"
str2 = "exam";

print(str1.index(str2))  # 7
print(str1.index(str2, 5))  # 7
# print (str1.index(str2, 10)) #异常

# ---------join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
# 语法：str.join(sequence)，返回通过指定字符连接序列中元素后生成的新字符串。
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "t", "x", "t")  # 字符串序列
print(s1.join(seq))  # r-u-n-t-x-t
print(s2.join(seq))  # runtxt

# --------- len() 方法返回对象（字符、列表、元组等）长度或项目个数
l = [1, 2, 3, 4, 5]
str = "runtxt"
print(len(str))  ## 字符串长度 5
print(len(l))  # 列表元素个数 5

# --------ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。
# 如果指定的长度小于原字符串的长度则返回原字符串
str = "example....wow!!!"
print(str.ljust(50, '*'))  # example....wow!!!*********************************

# --------lstrip() 方法用于截掉字符串左边的空格或指定字符
str = "     this is string example....wow!!!     ";
print(str.lstrip());  # this is string example....wow!!!
str = "88888888this is string example....wow!!!8888888";
print(str.lstrip('8'));  # this is string example....wow!!!8888888

# ---------replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，
# 如果指定第三个参数max，则替换不超过 max 次。
# 语法：str.replace(old, new[, max])
str = "www.baidu.com"
print("旧地址：", str)
print("新地址：", str.replace("baidu.com", "google.com"))

str = "this is string example....wow!!!"
print(str.replace("is", "was", 3))

# -------split() 通过指定分隔符对字符串进行切片，如果第二个参数 num 有指定值，则分割为 num+1 个子字符串
# 语法：str.split(str="", num=string.count(str))
#   str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
#   num -- 分割次数。默认为 -1, 即分隔所有
url = "http://www.baidu.com/python/image/123456.jpg"
path = url.split("/")  # 以“.” 进行分隔
print(path)  # ['http:', '', 'www.baidu.com', 'python', 'image', '123456.jpg']

txt = "Google#Runoob#Taobao#Facebook"
x = txt.split("#", 1)  # 第二个参数为 1，返回两个参数列表, 分割一次，返回2
print(x)

# -------swapcase() 方法用于对字符串的大小写字母进行转换
# str.swapcase();
str = "this Is string example....wow!!!"
print(str.swapcase())  # THIS iS STRING EXAMPLE....WOW!!!

'''
string.capitalize()
把字符串的第一个字符大写

string.center(width)
返回一个原字符串居中,并使用空格填充至长度 width 的新字符串

string.count(str, beg=0, end=len(string))
返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

string.decode(encoding='UTF-8', errors='strict')
以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 'ignore' 或 者'replace'

string.encode(encoding='UTF-8', errors='strict')
以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'

string.endswith(obj, beg=0, end=len(string))
检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.

string.expandtabs(tabsize=8)
把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。

string.find(str, beg=0, end=len(string))
检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1

string.format()
格式化字符串

string.index(str, beg=0, end=len(string))
跟find()方法一样，只不过如果str不在 string中会报一个异常.

string.isalnum()
如果 string 至少有一个字符并且所有字符都是字母或数字则返
回 True,否则返回 False

string.isalpha()
如果 string 至少有一个字符并且所有字符都是字母则返回 True,
否则返回 False

string.isdecimal()
如果 string 只包含十进制数字则返回 True 否则返回 False.

string.isdigit()
如果 string 只包含数字则返回 True 否则返回 False.

string.islower()
如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

string.isnumeric()
如果 string 中只包含数字字符，则返回 True，否则返回 False

string.isspace()
如果 string 中只包含空格，则返回 True，否则返回 False.

string.istitle()
如果 string 是标题化的(见 title())则返回 True，否则返回 False

string.isupper()
如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

string.join(seq)
以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

string.ljust(width)
返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串

string.lower()
转换 string 中所有大写字符为小写.

string.lstrip()
截掉 string 左边的空格

string.maketrans(intab, outtab])
maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

max(str)
返回字符串 str 中最大的字母。

min(str)
返回字符串 str 中最小的字母。

string.partition(str)
有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.

string.replace(str1, str2,  num=string.count(str1))
把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.

string.rfind(str, beg=0,end=len(string) )
类似于 find() 函数，返回字符串最后一次出现的位置，如果没有匹配项则返回 -1。

string.rindex( str, beg=0,end=len(string))
类似于 index()，不过是从右边开始.

string.rjust(width)
返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串

string.rpartition(str)
类似于 partition()函数,不过是从右边开始查找

string.rstrip()
删除 string 字符串末尾的空格.

string.split(str="", num=string.count(str))
以 str 为分隔符切片 string，如果 num 有指定值，则仅分隔 num+ 个子字符串

string.splitlines([keepends])
按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。

string.startswith(obj, beg=0,end=len(string))
检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.

string.strip([obj])
在 string 上执行 lstrip()和 rstrip()

string.swapcase()
翻转 string 中的大小写

string.title()
返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())

string.translate(str, del="")
根据 str 给出的表(包含 256 个字符)转换 string 的字符,
要过滤掉的字符放到 del 参数中

string.upper()
转换 string 中的小写字母为大写

string.zfill(width)
返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0
'''
