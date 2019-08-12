# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-08 14:20
# @Author  : lidong@immusician.com
# @Site    :
# @File    : 反射.py
import ujson

ret = isinstance("a", str)
print(ret)

dic = {"str": str}
ret = isinstance("a", dic["str"])
print(ret)

set_demo = {ujson.dumps({"1": "a"}), ujson.dumps({"2": "a"}), ujson.dumps({"1": "a"}), ujson.dumps({"2": "a"})}
print(set_demo)
