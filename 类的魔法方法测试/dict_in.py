#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : lidong@immusician.com
# @Site    :
# @File    :

dic = {
    "a": 1,
    "b": 1,
    "c": 1,
    "d": 1,
    "e": 1,
}

# print("ec" in dic)


class A:
    a = 1
    b = 2
    c = 3


s = A()
print(id(s))
print(hash(s))
print(hash(s) * 16)
# print("a" in s)

