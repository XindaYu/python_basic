#!/usr/bin/python3
# Filename: support.py

def print_func(par):
    print("Hello : ", par)
    return


def fib(n):  # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()
