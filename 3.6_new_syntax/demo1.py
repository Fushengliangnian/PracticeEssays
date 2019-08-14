#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : lidong@immusician.com
# @Site    :
# @File    :
import time
from typing import TypeVar


class A:
    pass


B = TypeVar("B", bound=A)


def fun(a: B):
    print(a())
    print(a, 777)
    time.time



# fun("A")
# fun(A())
fun(A)

ret = bool(1)
ret = bool(0)
print(ret)

