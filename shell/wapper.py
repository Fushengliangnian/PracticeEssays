# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-20 17:20
# @Author  : lidong@immusician.com
# @Site    :
# @File    : wapper.py


def wrapper(fun):
    def inner():
        print("执行被装饰函数之前")
        ret = fun()
        print("执行被装饰函数之后")
        return ret
    return inner


def func():
    print("func")


func()
print("")
wrapper(func)()
print("")


@wrapper
def func1():
    print("func1")


func1()
print()

# @ 叫做语法糖
# @wrapper  ==  wrapper(func)


def func2():
    print("func2")


@wrapper
@wrapper
def func3():
    print("func3")


wrapper(wrapper(func2))()
print()
func3()

