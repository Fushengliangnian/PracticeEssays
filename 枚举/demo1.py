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
# print(type(c))
# print(c.__dict__)
# print(c.name)

lis1 = [
    {"id": "a", "a1": 1},
    {"id": "b", "b1": 2},
    {"id": "c", "c1": 3},
    {"id": "d", "d1": 4},
    {"id": "e", "e1": 5},
]
lis2 = [
    {"id": "a", "a2": 11},
    {"id": "b", "b2": 22},
    {"id": "c", "c2": 33},
    {"id": "d", "d2": 44},
    {"id": "e", "e2": 55},
]

ret = zip(lis1, lis2)
# print(list(ret))
# res = filter(lambda x, y: x["a"] == y["a"], ret)
# print(list(res), ret)

for i in lis1:
    for j in lis2:
        if i["id"] == j["id"]:
            i.update(j)

print(lis1)
