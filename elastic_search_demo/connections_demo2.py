# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-09-03 10:00
# @Author  : lidong@immusician.com
# @Site    : 
# @File    : connections_demo2
from elasticsearch import Transport, Elasticsearch
from elasticsearch.connection import RequestsHttpConnection


def single_connect():
    es = Elasticsearch([{"host": "localhost", "port": 9200}])
    return es


def connect_pool():
    pool = Transport([{"host": "localhost", "port": 9200}], connection_class=RequestsHttpConnection).connection_pool
    conn = pool.get_connection()
    return conn


def get():
    # conn = connect_pool()
    conn = single_connect()
    ret = conn.get("zipkin:span-2019-05-16", "AWq_dR6Ht37NSJExPGhQ", doc_type="span")
    return ret


def search():
    conn = single_connect()
    ret = conn.search()
    return ret


def create():
    conn = single_connect()
    ret = conn.create()
    return ret


print(get())
print("**********")
print(search())
