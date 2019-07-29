#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : lidong@immusician.com
# @Site    :
# @File    :
from elasticsearch import Elasticsearch

es = Elasticsearch([{"host": "localhost", "port": 9200}])
print(es.info)

# 创建索引
# ret = es.indices.create(index="my-index", ignore=400)
# print(ret)

data = {
    "title": "头",
    "body": "身体",
}
# i = es.index("my-index", body=data, doc_type="collection")
# print(i)
ret = es.search(index="my-index")
print(ret)