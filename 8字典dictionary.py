# Dictionary（字典）
# 列表是有序的对象集合，字典是无序的对象集合。
# 字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：
#   d = {key1 : value1, key2 : value2, key3 : value3 }
#       键必须是唯一的(key)，必须使用不可变类型
#       值可以取任何数据类型，但键必须是不可变的，如字符串，数字

# 格式        1.大括号里逗号分隔，键值用冒号{  ： ，  ：  ，}
#             2.dict函数：dict( ('Runoob', 1),('Runoob', 1))
#                         dict( a=1 , b=2 )

# -----------init
dict1 = {'abc': 456}
dict2 = {'abc': 123, 98.6: 37}
dict0 = {}
dict0['one'] = "1 - aaa"
dict0[2] = "2 - bbb"

# 构造函数 dict() 可以直接从键值对序列中构建字典如下：
newdict1 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
newdict2 = dict(Runoob=1, Google=2, Taobao=3)
newdict3 = {x: x ** 2 for x in (2, 4, 6)}

print("newdict1 is: ", newdict1)  # {'Runoob': 1, 'Google': 2, 'Taobao': 3}
print("newdict2 is: ", newdict2)  # {'Runoob': 1, 'Google': 2, 'Taobao': 3}
print("newdict3 is: ", newdict3)  # {2: 4, 4: 16, 6: 36}

# -----------访问
dict3 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict3['Name'])
print("dict['Age']: ", dict3['Age'])
print("dictionary0 is: ", dict0)

# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

tinydict = {'name': 'runtest', 'code': 1, 'site': 'www.baidu.com'}
print(dict0['one'])  # 输出键为 'one' 的值 1 - aaa
print(dict0[2])  # 输出键为 2 的值 2 - bbb
print(tinydict)  # 输出完整的字典 {'name': 'runtest', 'code': 1, 'site': 'www.baidu.com'}
print(tinydict.keys())  # 输出所有键 dict_keys(['name', 'code', 'site'])
print(tinydict.values())  # 输出所有值 dict_values(['runtest', 1, 'www.baidu.com'])

# -----------修改字典
# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对
dict4 = {'Name': 'Run', 'Age': 7, 'Class': 'First'}
dict4['Age'] = 8  # 更新 Age
dict4['School'] = "教程"  # 添加信息

print("dict['Age']: ", dict4['Age'])
print("dict['School']: ", dict4['School'])

# -----------删除字典元素
# 能删单一的元素也能清空字典，清空只需一项操作，删除一个字典用del命令
dictdel1 = {'Name': 'wo', 'Age': 7, 'Class': 'First'}
dictdel2 = {'Name': 'wo', 'Age': 7, 'Class': 'First'}
del dictdel1['Name']  # 删除键 'Name'
print(dictdel1)

dictdel1.clear()  # 清空字典
print(dictdel1)

del dictdel2  # 删除字典
# print(dictdel2)

# ------------------字典键的特性
# 字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行

# 1.不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
dict = {'Name': 'old', 'Age': 7, 'Name': 'new'}
print("dict['Name']: ", dict['Name'])  # new

# 2.键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
# dict = {['Name']: 'Runoob', 'Age': 7}
# print("dict['Name']: ", dict['Name']) #wrong

# 字典类型也有一些内置的函数，例如clear()、keys()、values()等。
# 1	len(dict) 计算字典元素个数，即键的总
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("length: ", len(dict))  # 3

# 2	str(dict) 输出字典，以可打印的字符串表示
print(str(dict))  # {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

# 3	type(variable) 返回输入的变量类型，如果变量是字典就返回字典类
print(type(dict))  # <class 'dict'>

# ------------------内置方法
# 1	radiansdict.clear()
# 删除字典内所有元素
dict = {'Name': 'Zara', 'Age': 7}
print("字典长度 : %d" % len(dict))
dict.clear()
print("字典删除后长度 : %d" % len(dict))

# 2	radiansdict.copy()
# 返回一个字典的浅复制


# 3	radiansdict.fromkeys()
# 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值


# 4	radiansdict.get(key, default=None)
# 返回指定键的值，如果键不在字典中返回 default 设置的默认值


# 5	key in dict
# 如果键在字典dict里返回true，否则返回false
# Python 字典 in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
# 而 not in 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true
if 'Age' in dict:
    print("键 Age 存在")
else:
    print("键 Age 不存在")

# 6	radiansdict.items()
# 以列表返回可遍历的(键, 值) 元组数组


# 7	radiansdict.keys()
# 返回一个迭代器，可以使用 list() 来转换为列表


# 8	radiansdict.setdefault(key, default=None)
# 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default


# 9	radiansdict.update(dict2)
# 把字典dict2的键/值对更新到dict里


# 10	radiansdict.values()
# 返回一个迭代器，可以使用 list() 来转换为列表
dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
print("字典所有值为 : ", list(dict.values()))

# 11	pop(key[,default])
# 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值


# 12	popitem()
# 随机返回并删除字典中的最后一对键和值
