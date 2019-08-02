# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-02 10:13
# @Author  : lidong@immusician.com
# @Site    :
# @File    : demo1.py

from enum import IntEnum


class A(IntEnum):
    a = 1
    b = 2


c = A(1)
print(type(c))
print(c.__dict__)
print(c.name)
