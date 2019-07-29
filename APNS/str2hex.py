#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : lidong@immusician.com
# @Site    :
# @File    :

s = "sdffgss"
new = [hex(ord(ch)).replace('0x', chr(0x5c)+'x') for ch in s]
print(new)
# print(s)
# print(hex(s))
