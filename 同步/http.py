#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : lidong@immusician.com
# @Site    :
# @File    :

from requests import post


header = {
    "accept": "application/json",
    "content-type": "application/json",
    "UID": "78",
    "Token": "GOD"
}

data = {
    "purchase_receipt": '{"Store":"GooglePlay","TransactionID":"GPA.3389-5402-1788-52307","Payload":"{\"json\":\"{\\\"orderId\\\":\\\"GPA.3389-5402-1788-52307\\\",\\\"packageName\\\":\\\"com.okmusician.android\\\",\\\"productId\\\":\\\"okmusician.monthly.guitar\\\",\\\"purchaseTime\\\":1562583497223,\\\"purchaseState\\\":0,\\\"developerPayload\\\":\\\"{\\\\\\\"developerPayload\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"is_free_trial\\\\\\\":false,\\\\\\\"has_introductory_price_trial\\\\\\\":false,\\\\\\\"is_updated\\\\\\\":false}\\\",\\\"purchaseToken\\\":\\\"fganbdclakcielgchkpdappe.AO-J1OwFcdb640FCmQ3rND2zqc7Lnsji7mxcHR15GUlhl0FGreLreZgLOna82klyDsxHY25atmghS7az_gNT76ARtKMI6VsY3gIrU00cymW0bFPnf2NyU8LyYx9PQX9EX_w0A3i4rN9P2JEmaTNnwikHwTyYzYGRKw\\\",\\\"autoRenewing\\\":true}\",\"signature\":\"GqrT1HuB4fbq3djn6LS72MbWDI4qU4J0vzXV8t\\/quDEjUd8ZVJFdn\\/VZDjGcjoB7fRtNPCYGKlhlUb3YCHBq50ACtyDbGSAO0l+wyAEA0ueRvcFjFM6zpT7slnKktuTLwXll4+Ii\\/2ySL7Ny7pJcolYK6XNeEMHH3+as3iNIoMprMn9qKhdQyvcLsphQSfGAdO9mLxAvBqvR0DWCC2dooquJiw5BpNU5tg\\/Qb6ZuT8gIMr3z7NWs0bKBoPBttxnKgjN4rLaWUCcnH6Cqb8xRe017VoauqPKVQUYfbGVLf5aGBZcW9OtPFIZFQkSVlhPu3neuHtuwwc5Il+Rz2VEFTg==\",\"skuDetails\":\"{\\\"skuDetailsToken\\\":\\\"AEuhp4JB27Uvd5k7I7YEOktrYgWDaPDRQ8HbPrC4KKaSg-ydcNIfPENOJ_iZbXhAVgWk\\\",\\\"productId\\\":\\\"okmusician.monthly.guitar\\\",\\\"type\\\":\\\"subs\\\",\\\"price\\\":\\\"HK$78.00\\\",\\\"price_amount_micros\\\":78000000,\\\"price_currency_code\\\":\\\"HKD\\\",\\\"subscriptionPeriod\\\":\\\"P1M\\\",\\\"freeTrialPeriod\\\":\\\"P3D\\\",\\\"title\\\":\\\"Monthly Subscription for Guitar (OKMusician)\\\",\\\"description\\\":\\\"Fully access Guitar Lessons, Songs, Chord Library and Reverse Chord Finder.\\\"}\",\"isPurchaseHistorySupported\":true}"}'
}

ret = post("http://127.0.0.1:8001/v9/subscription/google/check", header=header, json=data)
print(ret.content)
