# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-06 13:49
# @Author  : lidong@immusician.com
# @Site    :
# @File    : read_json_file.py
import ujson

with open("./json_file.json", "rb") as f:
    ret = ujson.load(f)
    print(ret)
