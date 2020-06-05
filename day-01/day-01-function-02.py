# !/usr/bin/python3
# -*- coding: UTF-8 -*-


def outer():
    x = "local"
    print("outer:", x)
    def inner():
        nonlocal x # nonlocal关键字表示这里的x就是外部函数outer定义的变量x
        x = 'nonlocal'
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

# 闭包

