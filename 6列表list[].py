# List（列表）
# 列表可以完成大多数集合类的数据结构实现,列表都可以进行的操作包括索引，切片，加，乘，检查成员。
# 列表中元素的  ----+++++++类型可以不相同,可以改变+++++++---- ，它支持数字，字符串甚至可以包含列表（所谓嵌套)
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

# -----------更新列表,列表中的元素是可以改变的,可以使用 append() 方法来添加列表项
a = [1, 2, 3, 4, 5, 6]
a[0] = 0
a[2:5] = [13, 14, 15]
print(a)  # [9, 2, 13, 14, 15, 6]
a[2:5] = []  # 将对应的元素值设置为 []
print(a)  # [9, 2, 6]
a = [1, 2, 3, 4, 5, 6]

del a[2]
print("删除第三个元素", a)

# list.index(obj)
# 从列表中找出某个值第一个匹配项的索引位置
list1 = ['Google', 'Run', 'Taobao']
print('Runoob 索引值为', list1.index('Run'))
print('Taobao 索引值为', list1.index('Taobao'))

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

# 列表脚本操作符
# len([1, 2, 3])	3	长度
# [1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
# ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
# 3 in [1, 2, 3]	True	元素是否存在于列表中
# for x in [1, 2, 3]:
#   print(x, end=" ")	  #1 2 3	迭代

# 嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print("x 是: ", x)
print("x[0] 是: ", x[0])

# Python列表函数&方法
# 1	len(list)
list1 = ['Google', 'Runoob', 'Taobao']
print(len(list1))
list2 = list(range(5))  # 创建一个 0-4 的列表
print(len(list2))

# 2	max(list)
list1, list2 = ['Google', 'Run', 'Taobao'], [456, 700, 200]
print("list1 最大元素值 : ", max(list1))  # Taobao
print("list2 最大元素值 : ", max(list2))  # 700

# 3	min(list)
print("list1 最小元素值 : ", min(list1))  # Google
print("list2 最小元素值 : ", min(list2))  # 200

# 4	list(seq)

aTuple = (123, 'Google', 'Run', 'Taobao')
list1 = list(aTuple)
print("列表元素 : ", list1)  # [123, 'Google', 'Run', 'Taobao']

str = "Hello World"
list2 = list(str)
print("列表元素 : ", list2)  # ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

# Python包含以下方法:
# 1	list.append(obj)
# 在列表末尾添加新的对象
list1 = ['Google', 'Run', 'Taobao']
list1.append('Baidu')
print("更新后的列表 : ", list1)  # ['Google', 'Run', 'Taobao', 'Baidu']

# 2	list.count(obj)
# 统计某个元素在列表中出现的次数
aList = [123, 'Google', 'Run', 'Taobao', 123];
print("123 元素个数 : ", aList.count(123))  # 2
print("Run 元素个数 : ", aList.count('Run'))  # 1

# 3	list.extend(seq)
# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list1 = ['Google', 'Run', 'Taobao']
list2 = list(range(5))  # 创建 0-4 的列表
list1.extend(list2)  # 扩展列表
print("扩展后的列表：", list1)  # ['Google', 'Run', 'Taobao', 0, 1, 2, 3, 4]

# 4	list.index(obj)
# 从列表中找出某个值第一个匹配项的索引位置
list1 = ['Google', 'Run', 'Taobao']
print('Runoob 索引值为', list1.index('Run'))  # 1
print('Taobao 索引值为', list1.index('Taobao'))  # 2

# 5	list.insert(index, obj)
# 将对象插入列表
list1 = ['Google', 'Run', 'Taobao']
list1.insert(1, 'Baidu')
print('列表插入元素后为 : ', list1)  # ['Google', 'Baidu', 'Run', 'Taobao']

# 6	list.pop([index=-1])
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list1 = ['Google', 'Run', 'Taobao', 'abc']
list1.pop()
print("列表现在为 : ", list1)  # ['Google', 'Run', 'Taobao']
list1.pop(1)
print("列表现在为 : ", list1)  # ['Google', 'Taobao']

# 7	list.remove(obj)
# 移除列表中某个值的第一个匹配项
list1 = ['Google', 'Run', 'Taobao']
list1.remove('Run')
print("列表现在为 : ", list1)

# 8	list.reverse()
# 反向列表中元素
list1 = ['1', '2', 3]
list1.reverse()
print("列表反转后: ", list1)  # [3, '2', '1']

# 9	list.sort( key=None, reverse=False)
# 对原列表进行排序
aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
aList.sort()
print("List 排序: ", aList)  # ['Facebook', 'Google', 'Runoob', 'Taobao']

# 10	list.clear()
# 清空列表
list1 = ['Google', 'Taobao', 'Baidu']
list1.clear()
print("列表清空后 : ", list1)  # []

# 11	list.copy()
# 复制列表
list1 = ['Google', 'Run', 'Taobao', 'Baidu']
list2 = list1.copy()
print("list2 列表: ", list2)  # ['Google', 'Run', 'Taobao', 'Baidu']
