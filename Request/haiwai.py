#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : lidong@immusician.com
# @Site    :
# @File    :

from requests import post
import json

header = {
    "accept": "application/json",
    "content-type": "application/json",
    "UID": "519",
    "device-id": "4545",
    "Token": "GOD"
}

token = "bmmoccegpmlcnlkkanbkiecb.AO-J1OxmS9uIjLJynRU2TYV7T9tVXcNA8Xzh1LvYbaUFlryCtz9OWRYASRgw1_wY0igo-DLiaJ0gCP3yQeKohPKAhIl2i1mklgR53FD5g4k2MwDEUsurcDeI4hdFmEVTuR3NvnFftyLRKKXxuqoY7wO1bx8D9d9ytA"


data = {
    "purchase_receipt": json.dumps({"Store":"GooglePlay","TransactionID":"GPA.3342-2167-7425-48839","Payload":"{\"json\":\"{\\\"orderId\\\":\\\"GPA.3342-2167-7425-48839\\\",\\\"packageName\\\":\\\"com.okmusician.android\\\",\\\"productId\\\":\\\"okmusician.monthly.guitar\\\",\\\"purchaseTime\\\":1562596624964,\\\"purchaseState\\\":0,\\\"developerPayload\\\":\\\"{\\\\\\\"developerPayload\\\\\\\":\\\\\\\"\\\\\\\",\\\\\\\"is_free_trial\\\\\\\":false,\\\\\\\"has_introductory_price_trial\\\\\\\":false,\\\\\\\"is_updated\\\\\\\":false}\\\",\\\"purchaseToken\\\":\\\"bmmoccegpmlcnlkkanbkiecb.AO-J1OxmS9uIjLJynRU2TYV7T9tVXcNA8Xzh1LvYbaUFlryCtz9OWRYASRgw1_wY0igo-DLiaJ0gCP3yQeKohPKAhIl2i1mklgR53FD5g4k2MwDEUsurcDeI4hdFmEVTuR3NvnFftyLRKKXxuqoY7wO1bx8D9d9ytA\\\",\\\"autoRenewing\\\":true}\",\"signature\":\"TPghrGnYUGa8ocRFY6HftjpSPpWUvmxC4ZabxahDFFjBoku7xZutCGBbWx\\/tMO0\\/FX\\/r1ezuxHrbn2iKW8dFvOxQqwJ4VDIi\\/wBaFC4\\/mOmFUnh39ONMmn\\/3vnG4Gg25lb+YdC2ADjAcYuxAiZVy8ibm\\/qy8pQ7vxBOruHeIPpdskNQNczW8+KUi0XBaFvhp20\\/8yRCbGozKtRg8VagGMg1lIbcZqU8UXiqLdI+2TouldOsNhgP1mUdoUo4g4IOAg3HjHu2NOUvMn9og5QXZXPbfR+ji7Bed5xtFqUWMn0NZx7F56LHzzJPOcG2wrPyCbuj8cki++DWSFMw\\/T8kDoQ==\",\"skuDetails\":\"{\\\"skuDetailsToken\\\":\\\"AEuhp4KSErXXr6jINcbjSnDGt2tY1IBT5_lX2YowDXf78ivYH_jMYeocdhzPeKbF-9GV\\\",\\\"productId\\\":\\\"okmusician.monthly.guitar\\\",\\\"type\\\":\\\"subs\\\",\\\"price\\\":\\\"HK$78.00\\\",\\\"price_amount_micros\\\":78000000,\\\"price_currency_code\\\":\\\"HKD\\\",\\\"subscriptionPeriod\\\":\\\"P1M\\\",\\\"freeTrialPeriod\\\":\\\"P3D\\\",\\\"title\\\":\\\"Monthly Subscription for Guitar (OKMusician)\\\",\\\"description\\\":\\\"Fully access Guitar Lessons, Songs, Chord Library and Reverse Chord Finder.\\\"}\",\"isPurchaseHistorySupported\":true}"})
}

ret = post("http://127.0.0.1:8001/v9/subscription/google/check", headers=header, json=data)
print(ret.content)
