# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-01 17:54
# @Author  : lidong@immusician.com
# @Site    :
# @File    : aggregate_demo.py
from connections import live_music

data_statistics = live_music.v1_data_statistics


pipeline = [
    {"$match": {"result_data.game_type": 14}},
    {"$group": {"_id": "$result_data.lesson_id"}}
]
ret = data_statistics.aggregate(pipeline)
print(list(ret))
