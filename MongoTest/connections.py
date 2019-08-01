# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-01 17:51
# @Author  : lidong@immusician.com
# @Site    :
# @File    : connections.py

import pymongo

host = "192.168.1.120"
port = 30001

client = pymongo.MongoClient(host, port)
guitar = client.jita
live_music = client.livemusic
