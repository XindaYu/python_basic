# ===============================随机数函数================================================
# 随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
# Python包含以下常用随机数函数：
'''
函数	描述
choice(seq)
    从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])
    从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
random()
    随机生成下一个实数，它在[0,1)范围内。
seed([x])
    改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)
    将序列的所有元素随机排序
uniform(x, y)
    随机生成下一个实数，它在[x,y]范围内
'''

# -----------------------------------------------------------------------------
# --------------------------1.choice() 函数->选择一个字符
# choice() 方法返回一个列表，元组或字符串的随机项。语法：
# import random
# random.choice( seq  )
# 注意：choice()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。 seq -- 可以是一个列表，元组或字符串。

import random

print("从 range(100) 返回一个随机数 : ", random.choice(range(100)))
print("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))

# 小案例：--------------创建随机密码组合:--------------
import string  # string module里包含了阿拉伯数字,ascii码,特殊符号
import random  # 需要利用到choice

a = int(input('请输入要求的密码长度'))
b = string.digits + string.ascii_letters + string.punctuation  # 构建密码池
password = ""  # 命名一个字符串

for i in range(0, a):  # for loop 指定重复次数
    password = password + random.choice(b)  # 从密码池中随机挑选内容构建密码
print(password)  # 输出密码

# -----------------------------------------------------------------------------
# --------------------------2. randrange() 函数
# randrange() 方法返回指定递增基数集合中的一个随机数，基数默认值为1。从给定的范围返回随机项。语法：
# import random
# random.randrange ([start,] stop [,step])
# randrange()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
# 其中：start -- 指定范围内的开始值，包含在范围内。
# stop -- 指定范围内的结束值，不包含在范围内。
# step -- 指定递增基数
import random

# 从 1-100 中选取一个奇数
print("randrange(1,100, 2) : ", random.randrange(1, 100, 2))

# 从 0-99 选取一个随机数
print("randrange(100) : ", random.randrange(100))

# -----------------------------------------------------------------------------
# --------------------------3. random() 函数
# random() 方法返回随机生成的一个实数，它在[0,1)范围内。语法:
# import random
# random.random()

import random

# 第一个随机数
print("random() : ", random.random())

# 第二个随机数
print("random() : ", random.random())

# -----------------------------------------------------------------------------
# --------------------------4. seed() 函数
# seed() 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数,本函数没有返回值。 。
# 我们调用 random.random() 生成随机数时，每一次生成的数都是随机的。但是，当我们预先使用 random.seed(x)
# 设定好种子之后，其中的 x 可以是任意数字，如10，这个时候，先调用它的情况下，使用 random() 生成的随机数将会是同一个。

import random

random.seed()
print("使用默认种子生成随机数：", random.random())
print("使用默认种子生成随机数：", random.random())

random.seed(10)
print("使用整数 10 种子生成随机数：", random.random())
random.seed(10)
print("使用整数 10 种子生成随机数：", random.random())

random.seed("hello", 2)
print("使用字符串种子生成随机数：", random.random())

# -----------------------------------------------------------------------------
# --------------------------5. shuffle() 函数
# shuffle() 方法将序列的所有元素随机排序。返回 None。语法:
# import random
# random.shuffle (lst )

import random

list = [20, 16, 10, 5];
random.shuffle(list)
print("随机排序列表 : ", list)

random.shuffle(list)
print("随机排序列表 : ", list)

# -----------------------------------------------------------------------------
# --------------------------6. uniform() 函数
# uniform() 方法将随机生成下一个实数，它在 [x,y] 范围内,
# 返回一个浮点数 N，取值范围为如果 x<y 则 x <= N <= y，如果 y<x 则y <= N <= x。
# 语法:
# import random
# random.uniform(x, y)
# 参数 :x -- 随机数的最小值。y -- 随机数的最大值

import random

print("uniform(5, 10) 的随机浮点数 : ", random.uniform(5, 10))
print("uniform(7, 14) 的随机浮点数 : ", random.uniform(7, 14))
print("uniform(7, 14) 的随机浮点数 : ", round(random.uniform(5, 10), 2))  # 生成两位小数的浮点数
