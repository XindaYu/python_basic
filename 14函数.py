# ---------------------------函数
# 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
#
# 函数能提高应用的模块性，和代码的重复利用率。Python提供了许多内建函数，比如print()。
# 但也可以自己创建函数，这被叫做用户自定义函数。

# -----------------------------定义一个函数
# 规则：
# 代码块以 def 开头，接函数标识符名称 和圆括号 ()。
# 任何“传入参数”和“自变量”必须放在圆括号中间，圆括号之间可以用于定义参数。
# 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
# 函数内容以冒号 : 起始，并且缩进。
# return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。

# 语法：
# Python 定义函数使用 def 关键字，一般格式如下：
'''
def 函数名（参数列表）:
     函数体
'''


# 默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的
def hello():
    print("Hello World!")


hello()


# 比较两个数，并返回较大的数:
def max(a, b):
    if a > b:
        return a
    else:
        return b


a = 4
b = 5
print(max(a, b))


# 计算面积函数
def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("calculate area:")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))


# -----------------------------函数调用
# 定义函数
def printme(str):
    # 打印任何传入的字符串
    print(str)
    return


# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")


# ---------------------------参数
# 以下是调用函数时可使用的正式参数类型：
#   必需参数
#   关键字参数
#   默认参数
#   不定长参数

# 1.必需参数
# 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
# 调用 printme() 函数，你必须传入一个参数，不然会出现语法错误
# 可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return


# 调用 printme 函数，不加参数会报错
# printme() #会报错
printme("print abc")


# 2.关键字参数
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
# 以下实例在函数 printme() 调用时使用参数名:
# 可写函数说明
def printme(str):
    # "打印任何传入的字符串"
    print(str)
    return


# 调用printme函数
printme(str="可写函数说明")


# 可写函数说明
def printinfo(name, age):
    # "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="不用先后顺序")


# 3.默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值：
# 可写函数说明
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="name")
print("------------------------")
printinfo(name="name")


# 4. 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，
# 和上述 2 种参数不同，声明时不会命名。
# 4.1 基本语法如下 参数带*号：
# def functionname([formal_args,] *var_args_tuple ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)


# 输出:
# 70
# (60, 50)
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数


# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)


# 输出:
# 10
# 输出:
# 70
# 60
# 50
# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量

# 4.2 还有一种就是参数带两个星号 **基本语法如下 ：
# 加了两个星号 ** 的参数会以字典的形式导入
# def functionname([formal_args,] **var_args_dict ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
# 可写函数说明
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)


# 4.3 声明函数时，参数中星号 * 可以单独出现
# def f(a,b,*,c):
#     return a+b+c
# 如果单独出现星号 * 后的参数必须用关键字传入

def f(a, b, *, c):
    return a + b + c


# f(1,2,3)   # 报错
print(f(1, 2, c=3))  # 正常 6


# ----------------return语句
# return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。
# 不带参数值的return语句返回None。之前的例子都没有示范如何返回数值，以下实例演示了 return 语句的用法：
# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


# 调用sum函数
total = sum(10, 20)
print("函数外 : ", total)


# ---------------强制位置参数
# Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
# 在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参:
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


# 以下使用方法是正确的:
#
f(10, 20, 30, d=40, e=50, f=60)
# 以下使用方法会发生错误:
#
# f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
# f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式
