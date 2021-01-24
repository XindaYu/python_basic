#IF STATEMENT
'''
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
'''
# 如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句
# 如果 "condition_1" 为False，将判断 "condition_2"
# 如果"condition_2" 为 True 将执行 "statement_block_2" 块语句
# 如果 "condition_2" 为False，将执行"statement_block_3"块语句
# Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。

# PS:
# 1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
# 2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
# 3、在Python中没有switch – case语句

var1=100
if var1:
    print("1-if si true")
    print(var1)

var2 =0
if var2:
    print("2-if is true")
    print(var2)
print("bye!")

# <	小于
# <=	小于或等于
# >	大于
# >=	大于或等于
# ==	等于，比较两个值是否相等
# !=	不等于

# if 嵌套
# 在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中
# if 表达式1:
#     语句
#     if 表达式2:
#         语句
#     elif 表达式3:
#         语句
#     else:
#         语句
# elif 表达式4:
#     语句
# else:
#     语句
num=int(input("输入一个数字："))
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")

