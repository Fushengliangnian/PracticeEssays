# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-28 17:57
# @Author  : lidong@immusician.com
# @Site    :
# @File    : isinstance_json.py
import json

dic = {"a": "b"}

data = json.dumps(dic)
if isinstance(data, str):
    print(111)

