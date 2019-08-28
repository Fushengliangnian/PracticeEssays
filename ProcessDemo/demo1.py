# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-27 11:18
# @Author  : lidong@immusician.com
# @Site    :
# @File    : demo1.py

from multiprocessing import Process
import time


def fun(s):
    a = time.process_time()
    print("a :", a)
    time.sleep(2)
    b = time.process_time()
    print("b :", b)
    print("b-a :", b-a)


if __name__ == '__main__':
    new = time.time()
    p = Process(target=fun, args=(2, ))
    p.start()
    print(time.time() - new)
