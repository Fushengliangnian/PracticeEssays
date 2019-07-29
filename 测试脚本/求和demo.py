#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : lidong@immusician.com
# @Site    :
# @File    :

data = [
    {"a": 1, "b": 2},
    {"a": 1, "b": 2},
    {"a": 1, "b": 2},
    {"a": 1, "b": 2},
]


def fun(a, b, *args):
    print(a, b)
    print(args)


fun(1, 2, *[])
