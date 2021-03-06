# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数

a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b  # a, b = b, a+b 的计算方式为先计算右边表达式，然后同时赋值给左边

# end 关键字
# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
