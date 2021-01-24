# 循环语句
# while 判断条件(condition)：
#     执行语句(statements)……
# PS:同样需要注意冒号和缩进。在 Python 中没有 do..while 循环

# while for语句
# range()函数
# pass 语句

# -----------使用了 while 来计算 1 到 100 的总和
n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))

# ------------无限循环
'''
var = 1
while var == 1 :  # 表达式永远为 true
   num = int(input("输入一个数字  :"))
   print ("你输入的数字是: ", num)
 
print ("Good bye!")

输入一个数字  :5
你输入的数字是:  5
输入一个数字  :

注：可以使用 CTRL+C 来退出当前的无限循环
无限循环在服务器上客户端的实时请求非常有用
'''

# while 循环使用 else 语句
# 在 while … else 在条件语句为 false 时执行 else 的语句块。
# 语法格式如下：
# while <expr>:
#     <statement(s)>
# else:
#     <additional_statement(s)>

# 循环输出数字，并判断大小
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")

# ---------------简单语句组
# 类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示：

# flag = 1
# while (flag): print ('欢迎访问菜鸟教程!')
# print ("Good bye!")
# 可以使用 CTRL+C 来中断循环

# ----------------for 语句
# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
# for循环的一般格式如下：
# for <variable> in <sequence>:
#     <statements>
# else:
#     <statements>

languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)

sites = ["Baidu", "Google", "tiaochu", "Taobao"]
for site in sites:
    if site == "tiaochu":
        print("跳出!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

# --------range()函数
# 如果需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:
#
# 实例
print("rang函数遍历数字序列：")
for i in range(5):
    print(i, end="")

print("\nrang函数遍历区间数字序列：")
for i in range(5, 9):
    print(i, end=" ")

print("\nrang函数遍历有增量的区间数字序列：")
for i in range(0, 10, 3):
    print(i, end=" ")

print("\nrang函数遍历有增量的负数区间数字序列：")
for i in range(-10, -100, -30):
    print(i, end=" ")

print("\nrange()和len()函数以遍历一个序列的索引:")
a = ['Google', 'Baidu', 'sougou', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

# 使用range()函数来创建一个列表
print(list(range(5)))

# break 和 continue 语句及循环中的 else 子句
# while 中使用 break：
print("while 中使用 break:")
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')

# while 中使用 continue:
print("while 中使用 continue:")
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')

# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，
# 但循环被 break 终止时不执行。
#
# 如下实例用于查询质数的循环例子
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n // x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

#  pass是空语句，是为了保持程序结构的完整性。
#
# pass 不做任何事情，一般用做占位语句
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")
