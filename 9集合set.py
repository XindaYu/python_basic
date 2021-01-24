# 集合（set）
# 是一个无序的不重复元素序列
# 可以使用大括号 { } 或者 set() 函数创建集合，
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
# 格式：
#       parame = {value01,value02,...}
# or    set(value)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # {'pear', 'apple', 'orange', 'banana'}

a = set('abracadabra')
b = set('alacazam')

print(a)
print(" a - b:", a - b)  # 集合a中包含而集合b中不包含的元素{'r', 'd', 'b'}
print(a | b)  # 集合a或b中包含的所有元素{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a & b)  # 集合a和b中都包含了的元素{'a', 'c'}
print(a ^ b)  # 不同时包含于a和b的元素{'r', 'd', 'b', 'm', 'z', 'l'}

a = {x for x in 'abracadabra' if x not in 'abc'}
print("集合推导式:", a)  # {'r', 'd'}

# -----------------------------基本操作
# -------------------------1、添加元素
#  s.add( x ) 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作
thisset = set(("Google", "Runtest", "Taobao"))
thisset.add("Facebook")
print(thisset)  # {'Taobao', 'Facebook', 'Google', 'Runtest'}
# thisset.add([1,2])  #TypeError: unhashable type: 'list'

# s.update( x )以添加元素，且参数可以是列表，元组，字典等
thisset.update({1, 3})
print(thisset)  # {1, 'Runtest', 'Taobao', 3, 'Facebook', 'Google'}
thisset.update([1, 4], [5, 6])
print(thisset)  # {1, 'Taobao', 3, 4, 5, 6, 'Facebook', 'Runtest', 'Google'}

# -------------------------2、移除元素
# s.remove( x ) 将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误
# {1, 'Taobao', 3, 4, 5, 6, 'Facebook', 'Runtest', 'Google'}
thisset.remove("Taobao")
print(thisset)  # {1, 3, 4, 5, 6, 'Google', 'Facebook', 'Runtest'}
# thisset.remove("Taobao") #不存在时会发生错误 KeyError: 'Taobao'

# s.discard( x ) 移除集合中的元素，且如果元素不存在，不会发生错误
thisset.discard("Taobao")  # 不存在不会发生错误
print(thisset)  # {1, 3, 4, 5, 6, 'Google', 'Facebook', 'Runtest'}

# s.pop() 可以设置随机删除集合中的一个元素
thisset = set(("Google", "Run", "Taobao", "Facebook"))
x = thisset.pop()  # 删除的元素是什么
print("pop the value: ", x)
# set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除

# -------------------------3、计算集合元素个数
# len(s)
thisset = set(("Google", "Run", "Taobao"))
print("length is: ", len(thisset))  # 3

# -------------------------4、清空集合
# s.clear()
thisset = set(("Google", "Runoob", "Taobao"))
thisset.clear()
print(thisset)  # set()

# -------------------------5、判断元素是否在集合中存在
# x in s
thisset = set(("Google", "Run", "Taobao"))
print("Run" in thisset)  # True
print("Facebook" in thisset)  # False

# 完整方法：
# add()	为集合添加元素
# clear()	移除集合中的所有元素
# copy()	拷贝一个集合
# difference()	返回多个集合的差集
# difference_update()	移除集合中的元素，该元素在指定的集合也存在。
# discard()	删除集合中指定的元素
# intersection()	返回集合的交集
# intersection_update()	返回集合的交集。
# isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
# issubset()	判断指定集合是否为该方法参数集合的子集。
# issuperset()	判断该方法的参数集合是否为指定集合的子集
# pop()	随机移除元素
# remove()	移除指定元素
# symmetric_difference()	返回两个集合中不重复的元素集合。
# symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
# union()	返回两个集合的并集
# update()	给集合添加元素
