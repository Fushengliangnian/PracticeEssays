# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-07 15:33
# @Author  : lidong@immusician.com
# @Site    :
# @File    : demo2.py
import redis
import ujson

ret = redis.Redis()
ret.hset("ab", 1, ujson.dumps({"a": "a", "order": 0}))
ret.hset("ab", 3, ujson.dumps({"a": "a", "order": 2}))
ret.hset("ab", 2, ujson.dumps({"a": "a", "order": 1}))

obj = ret.hgetall("ab")
ret = sorted(obj.values(), key=lambda x: ujson.loads(x)["order"])
print(obj)
print(ret)
