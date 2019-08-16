# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-16 10:07
# @Author  : lidong@immusician.com
# @Site    :
# @File    : one_line_code_quick_sort.py


def qs(a):
    return qs([i for i in a[1:] if i <= a[0]]) + a[0:1] + qs([i for i in a[1:] if i > a[0]]) if len(a) > 1 else a

