# Number（数字）
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

# ========================================================================数学函数
# ****************abs(x)****************
# 返回数字的绝对值，如abs(-10) 返回 10
print("abs(-40) : ", abs(-40))  # abs(-40) :  40

# ****************ceil(x)****************
# 返回数字的上入整数，如math.ceil(4.1) 返回 5，ceil()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法
import math  # 导入 math 模块

print("math.ceil(-45.17) : ", math.ceil(-45.17))  # -45
print("math.ceil(100.12) : ", math.ceil(100.12))  # 101
print("math.ceil(100.72) : ", math.ceil(100.72))  # 101
print("math.ceil(math.pi) : ", math.ceil(math.pi))  # 4
# ****************(x>y)-(x<y)****************
# 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1

# ****************exp(x)****************
# 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
import math  # 导入 math 模块

print("math.exp(-45.17) : ", math.exp(-45.17))  # 2.4150062132629406e-20

# ****************fabs(x)****************
# 返回数字的绝对值，如math.fabs(-10) 返回10.0
# import math   # 导入 math 模块
print("math.fabs(-45.17) : ", math.fabs(-45.17))  # 45.17

# ****************floor(x)****************
# 返回数字的下舍整数，如math.floor(4.9)返回 4
# import math
print("math.floor(-45.17) : ", math.floor(-45.17))  # -46

# ****************log(x)****************
# 如math.log(math.e)返回1.0,math.log(100,10)返回2.0
# import math
print("math.log(100.12) : ", math.log(100.12))  # 4.6063694665635735

# ****************log10(x)****************
# 返回以10为基数的x的对数，如math.log10(100)返回 2.0
# import math
print("math.log10(100.12) : ", math.log10(100.12))  # 2.0005208409361854

# ****************max(x1, x2,...)****************
# 返回给定参数的最大值，参数可以为序列。
# import math
print("max(80, 100, 1000) : ", max(80, 100, 1000))  # 1000

# ****************min(x1, x2,...)****************
# 返回给定参数的最小值，参数可以为序列。
# import math
print("min(80, 100, 1000) : ", min(80, 100, 1000))  # 80

# ****************modf(x)****************
# 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
# import math
print("math.modf(100.12) : ", math.modf(100.12))  # (0.12000000000000455, 100.0)
print("-math.modf(-math.pi) : ", math.modf(-math.pi))  # (-0.14159265358979312, -3.0)

# ********************pow(x, y)*******************
# x**y 运算后的值。
# ****************内置的pow() 方法*****************
# pow(x, y[, z])函数是计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z
# pow() 通过内置的方法直接调用，内置方法会把参数作为整型，而 math 模块则会把参数转换为 float
# import math
print("math.pow(100, 2) : ", math.pow(100, 2))  # 10000.0
print("pow(100, 2) : ", pow(100, 2))  # 10000

# ****************round(x [,n])****************
# 返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。
# 其实准确的说是保留值将保留到离上一位更近的一端。
# 不用XX math
print("round(70.23456) : ", round(70.23456))  # 70
print("round(2.675, 2) : ", round(2.675, 2))  # 2.67
# 这跟浮点数的精度有关。在机器中浮点数不一定能精确表达，因为换算成一串 1 和 0 后可能是无限位数的，
# 机器已经做出了截断处理。那么在机器中保存的2.675这个数字就比实际数字要小那么一点点。
# 这一点点就导致了它离 2.67 要更近一点点，所以保留两位小数时就近似到了 2.67。

# ****************sqrt(x)****************
# 返回数字x的平方根。
# import math
print("math.sqrt(100) : ", math.sqrt(100))  # 10.0

# ========================================================================三角函数
'''
函数	描述
acos(x)	
    返回x的反余弦弧度值。x -- -1到1之间的数值。如果x是大于1，会产生一个错误。需要导入 math 模块
asin(x)	返回x的反正弦弧度值，需要导入 math 模块 。
atan(x)	返回x的反正切弧度值，需要导入 math 模块 。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值，需要导入 math 模块 。
cos(x)	返回x的弧度的余弦值，需要导入 math 模块 。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)，需要导入 math 模块。
sin(x)	返回的x弧度的正弦值，需要导入 math 模块。
tan(x)	返回x弧度的正切值。返回 x 弧度的正切值，数值在 -1 到 1 之间，需要导入 math 模块。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	
    将角度转换为弧度
    角度和弧度关系是：2π 弧度 = 360°。从而 1°≈0.0174533 弧度，1 弧度≈57.29578°。
        1)角度转换为弧度公式：弧度=角度÷180×π
        2)弧度转换为角度公式： 角度=弧度×180÷π
'''
import math

print("acos(0.64) : ", math.acos(0.64))
print("asin(0.64) : ", math.asin(0.64))
print("atan(0.64) : ", math.atan(0.64))

print("atan2(-0.50,-0.50) : ", math.atan2(-0.50, -0.50))
print("cos(2*math.pi) : ", math.cos(2 * math.pi))
print("hypot(-3, 3) : ", math.hypot(-3, 3))
print("sin(math.pi/2) : ", math.sin(math.pi / 2))
print("tan(math.pi) : ", math.tan(math.pi))
print("degrees(3) : ", math.degrees(3))  # 171.88733853924697

print("radians(90) : ", math.radians(90))  # 1 弧度等于大概 57.3°
print("radians(45) : ", math.radians(45))
print("radians(30) : ", math.radians(30))
print("radians(180) : ", math.radians(180))  # 180 度的弧度为 π

print("180 / pi : ", end="")
print(math.radians(180 / math.pi))

# 数学常量
# pi	数学常量 pi（圆周率，一般以π来表示）
# e	数学常量 e，e即自然常数（自然常数）。
