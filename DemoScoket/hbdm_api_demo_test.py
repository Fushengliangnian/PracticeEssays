#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 15:48:13 2018
@author: zhaobo
"""

from views.HuobiDMService import HuobiDM
from pprint import pprint

#### input huobi dm url
# URL = 'https://api.hbdm.com'
URL = 'https://api.huobi.pro'

####  input your access_key and secret_key below:
ACCESS_KEY = 'afwo04df3f-369e37f8-3be3d3b7-8ea8f'
SECRET_KEY = 'f8575ea3-da04ee60-5fe3f984-a7b0d'

ACCESS_KEY_one = '1ebe32b2-bewr5drtmh-f16ecbe7-2306a'
SECRET_KEY_one = '0d83a484-ee266ee9-a9aa83ba-ddf0a'

dm = HuobiDM(URL, ACCESS_KEY, SECRET_KEY)

# another account:
dm2 = HuobiDM(URL, ACCESS_KEY_one, SECRET_KEY_one)

# 获取账户id
print("获取账户id")

account_id = dm.get_common_account_accounts()["data"][0]["id"]
account_id_two = dm2.get_common_account_accounts()["data"][0]["id"]
print(account_id, account_id_two)

import time, random, multiprocessing
from multiprocessing import Process

#
n_total = 0  # 策略一买的总价格
n1_total = 0  # 策略一卖的总价格
n2_total = 0  # 策略二买的总价格
n3_total = 0  # 策略卖的总价格
n4_total = 0
n5_total = 0
total_amount = 0  # 总得交易额

buy_amount_total = 0  # 策略一第一轮买的总数量
buy2_amount_total = 0  # 策略一第二轮买的总数量
sell_amount_total = 0  # 策略一第一轮卖的总数量
sell2_amount_total = 0  # 策略一第二轮卖的总数量
buy3_amount_total = 0  # 策略二第一轮买的总数量
buy4_amount_total = 0  # 策略二第二轮买的总数量
sell3_amount_total = 0  # 策略二第一轮卖的总数量
sell4_amount_total = 0  # 策略二第二 轮卖的总数量
count_num = 0

print("开始")

while total_amount < 500000:
    buyone_price_ucbtc = dm.get_contract_market_merged_spot("ucbtc")["tick"]["bid"][0]  # 买一的价格
    sellone_price_ucbtc = dm.get_contract_market_merged_spot("ucbtc")["tick"]["ask"][0]  # 卖一的价格

    buyone_number_ucbtc = dm.get_contract_market_merged_spot("ucbtc")["tick"]["bid"][1]  # 买一挂单的数量

    sellone_number_ucbtc = dm.get_contract_market_merged_spot("ucbtc")["tick"]["ask"][1]  # 卖一的数量:交易对:ucbtc

    # 策略一
    if buy_amount_total >= 500 and sell_amount_total >= 500:
        buy_amount_total = 0
        sell_amount_total = 0

    if buy2_amount_total >= 500 and sell2_amount_total >= 500:
        buy2_amount_total = 0
        sell2_amount_total = 0

    if buy3_amount_total >= 500 and sell3_amount_total >= 500:
        buy3_amount_total = 0
        sell3_amount_total = 0

    if buy4_amount_total >= 500 and sell4_amount_total >= 500:
        buy4_amount_total = 0
        sell4_amount_total = 0

    # print("策略一的买卖")
    while 500 > buy_amount_total >= 0 and 500 > sell_amount_total >= 0 and sellone_price_ucbtc - buyone_price_ucbtc >= 0.02e-08:
        amount = random.randint(30, 50)
        price = round(random.uniform(buyone_price_ucbtc + 0.01e-08, sellone_price_ucbtc - 0.01e-08), 10)  # 获取随机价格

        n = price * amount
        n_total += n
        print("本次价格:" + str(price))
        print("本次数量:" + str(amount))
        # print("买入总价格是" + str(n_total))

        sell_amount_total = round(sell_amount_total + amount, 2)

        # 开始下单,并更新数据
        print(dm.send_contract_order_place(str(account_id), "ucbtc", "sell-limit", str(amount), str(price), "api"),
              dm2.send_contract_order_place(str(account_id_two), "ucbtc", "buy-limit", str(amount), str(price), "api"))
        count_num += 1
        print("第" + str(count_num) + "次交易")
        # print(dm2.send_contract_order_place(str(account_id_two), "ucbtc", "buy-limit", str(amount), str(price), "api"))
        # n1 = price * amount
        # n1_total += n1

        buy_amount_total = round(buy_amount_total + amount, 2)

        buyone_price_ucbtc = dm.get_contract_market_merged_spot("ucbtc")["tick"]["bid"][0]  # 买一的价格
        sellone_price_ucbtc = dm.get_contract_market_merged_spot("ucbtc")["tick"]["ask"][0]  # 卖一的价格

        price = round(random.uniform(buyone_price_ucbtc + 0.01e-08, sellone_price_ucbtc - 0.01e-08), 10)  # 获取随机价格

        time.sleep(1.5)

    while 500 > buy2_amount_total >= 0 and 500 > sell2_amount_total >= 0 and sellone_price_ucbtc - buyone_price_ucbtc >= 0.02e-08:
        amount = random.randint(30, 50)
        price = round(random.uniform(buyone_price_ucbtc + 0.01e-08, sellone_price_ucbtc - 0.01e-08), 10)  # 获取随机价格

        n2 = price * amount
        n2_total += n2
        print("本次价格:" + str(price))
        print("本次数量:" + str(amount))
        print("买入总价格是" + str(n2_total))

        sell2_amount_total = round(sell2_amount_total + amount, 2)

        # 开始下单,并更新数据
        print(dm2.send_contract_order_place(str(account_id_two), "ucbtc", "sell-limit", str(amount), str(price), "api"),
              dm.send_contract_order_place(str(account_id), "ucbtc", "buy-limit", str(amount), str(price), "api"))
        count_num += 1
        print("第" + str(count_num) + "次交易")
        # print(dm.send_contract_order_place(str(account_id), "ucbtc", "buy-limit", str(amount), str(price), "api"))
        n3 = price * amount
        n3_total += n3

        buy2_amount_total = round(buy2_amount_total + amount, 2)

        buyone_price_ucbtc = dm.get_contract_market_merged_spot("ucbtc")["tick"]["bid"][0]  # 买一的价格
        sellone_price_ucbtc = dm.get_contract_market_merged_spot("ucbtc")["tick"]["ask"][0]  # 卖一的价格

        price = round(random.uniform(buyone_price_ucbtc + 0.01e-08, sellone_price_ucbtc - 0.01e-08), 10)  # 获取随机价格

        time.sleep(1)

    # 策略二

    while 500 > sell3_amount_total >= 0 and 0.02e-08 > sellone_price_ucbtc - buyone_price_ucbtc >= 0.01e-08 and (
            sellone_number_ucbtc < 10 or buyone_number_ucbtc < 10):
        if buyone_number_ucbtc < 10:
            price = buyone_price_ucbtc
        elif sellone_number_ucbtc < 10:
            price = sellone_price_ucbtc
        amount = random.randint(30, 50)

        n4 = price * amount
        n4_total += n4

        print("本次价格:" + str(price))
        print("本次数量:" + str(amount))
        print("买入总价格是" + str(n4_total))

        sell3_amount_total = round((sell3_amount_total + amount), 2)

        # 开始下单,并更新数据
        print(dm.send_contract_order_place(str(account_id), "ucbtc", "sell-limit", str(amount), str(price), "api"),
              dm2.send_contract_order_place(str(account_id_two), "ucbtc", "buy-limit", str(amount), str(price), "api"))

        count_num += 1
        print("第" + str(count_num) + "次交易")
        # print(dm2.send_contract_order_place(str(account_id_two), "ucbtc", "buy-limit", str(amount), str(price), "api"))

        buy3_amount_total = round(buy3_amount_total + amount, 2)

        buyone_price_ucbtc = dm.get_contract_market_merged_spot("ucbtc")["tick"]["bid"][0]  # 买一的价格
        sellone_price_ucbtc = dm.get_contract_market_merged_spot("ucbtc")["tick"]["ask"][0]  # 卖一的价格

        buyone_number_ucbtc = dm.get_contract_market_merged_spot("ucbtc")["tick"]["bid"][1]  # 买一挂单的数量

        sellone_number_ucbtc = dm.get_contract_market_merged_spot("ucbtc")["tick"]["ask"][1]  # 卖一的数量:交易对:ucbtc
        price = round(random.uniform(buyone_price_ucbtc + 0.01e-08, sellone_price_ucbtc - 0.01e-08), 10)  # 获取随机价格

        time.sleep(1)

    while 500 > buy4_amount_total >= 0 and 0.02e-08 > sellone_price_ucbtc - buyone_price_ucbtc >= 0.01e-08 and (
            sellone_number_ucbtc < 10 or buyone_number_ucbtc < 10):
        if buyone_number_ucbtc < 10:
            price = buyone_price_ucbtc
        elif sellone_number_ucbtc < 10:
            price = sellone_price_ucbtc
        amount = random.randint(30, 50)

        n5 = price * amount
        n5_total += n5

        print("本次价格:" + str(price))
        print("本次数量:" + str(amount))
        print("买入总价格是" + str(n5_total))

        sell4_amount_total = round((sell4_amount_total + amount), 2)

        # 开始下单,并更新数据
        print(dm2.send_contract_order_place(str(account_id_two), "ucbtc", "sell-limit", str(amount), str(price), "api"),
              dm.send_contract_order_place(str(account_id), "ucbtc", "buy-limit", str(amount), str(price), "api"))
        count_num += 1
        print("第" + str(count_num) + "次交易")

        # print(dm.send_contract_order_place(str(account_id), "ucbtc", "buy-limit", str(amount), str(price),"api"))

        buy4_amount_total = round(buy4_amount_total + amount, 2)

        buyone_price_ucbtc = dm.get_contract_market_merged_spot("ucbtc")["tick"]["bid"][0]  # 买一的价格
        sellone_price_ucbtc = dm.get_contract_market_merged_spot("ucbtc")["tick"]["ask"][0]  # 卖一的价格

        buyone_number_ucbtc = dm.get_contract_market_merged_spot("ucbtc")["tick"]["bid"][1]  # 买一挂单的数量

        sellone_number_ucbtc = dm.get_contract_market_merged_spot("ucbtc")["tick"]["ask"][1]  # 卖一的数量:交易对:ucbtc
        price = round(random.uniform(buyone_price_ucbtc + 0.01e-08, sellone_price_ucbtc - 0.01e-08), 10)  # 获取随机价格

        time.sleep(1)

    total_amount = total_amount + buy_amount_total + sell_amount_total + buy2_amount_total + sell2_amount_total + buy3_amount_total + buy4_amount_total + sell3_amount_total + sell4_amount_total
