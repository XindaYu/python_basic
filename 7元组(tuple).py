# 元组（tuple）
# 元组写在----------小括号()里,元素不能修改---------
# 元素之间用逗号隔开, 元组中的元素类型也可以不相同

# -------------create创建
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"  # 不需要括号也可以
print("tup3类型是：", type(tup3))

tup4 = (50)
print("tup4类型是：", type(tup4))  # 不加逗号，类型为整型

tup5 = (50,)
print("tup5类型是：", type(tup5))  # 加上逗号，类型为元组

# --------------索引index
tuple0 = ('abcd', 786, 2.23, 'runtest', 70.2)
tinytuple = (123, 'runtest')

print(tuple0)  # 输出完整元组('abcd', 786, 2.23, 'runtest', 70.2)
print(tuple0[0])  # 输出元组的第一个元素abcd
print(tuple0[1:3])  # 输出从第二个元素开始到第三个元素(786, 2.23)
print(tuple0[2:])  # 输出从第三个元素开始的所有元素(2.23, 'runtest', 70.2)
print(tinytuple * 2)  # 输出两次元组(123, 'runtest', 123, 'runtest')
print(tuple0 + tinytuple)  # 连接元组('abcd', 786, 2.23, 'runtest', 70.2, 123, 'runtest')

# ----------------修改元组
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合

# tuple[0]=1    -># 修改元组元素的操作是非法的

# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = ()  # 空元组（0个元素）
tup2 = (20,)  # 一个元素，需要在元素后添加逗号

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print("拼接后的tuple: ", tup3)

# -------------删除元组delete
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tup = ('Google', 'Run', 1997, 2000)

print(tup)
del tup
print("删除后的元组 tup : ")  # 已删除
# print(tup) Traceback (most recent call last):
#   File "D:/Code/pythoncode/Python_summary/7元组(tuple).py", line 51, in <module>
#     print(tup)
# NameError: name 'tup' is not defined

# ---------元组运算符
# len((1, 2, 3))	3	计算元素个数
# (1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	连接
# ('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
# 3 in (1, 2, 3)	True	元素是否存在
# for x in (1, 2, 3): print (x,)	1 2 3	迭代


# ---------------内置函数
# 1	len(tuple)
# 计算元组元素个数
tuple1 = ('Google', 'Taobao', 2)
print(len(tuple1))  # 3

# 2	max(tuple)
# 返回元组中元素最大值
tuple2 = ('5', '4', '8')
print(max(tuple2))  # 8

# 3	min(tuple)
# 返回元组中元素最小值
print(min(tuple2))

# 4	tuple(iterable)
# 将可迭代系列转换为元组
list1 = ['Google', 'Taobao', 'mooc', 'Baidu']
tuple3 = tuple(list1)
print(tuple3)  # ('Google', 'Taobao', 'Runoob', 'Baidu')
# ps: 在上述调用tuple()函数时，要注意，之前不可以把tuple命名为一个元组数据元素，不然会报错

print(id(tup1))  # 读取内存地址
