#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : lidong@immusician.com
# @Site    :
# @File    :
import time

DELAY_HOURS = 1
DELAY_DAY = 24
DELAY_MONTH = 648
QUEUE = []
EXPIRES_PERIOD_YEAR = 12 * 648
EXPIRES_PERIOD_MONTH = 720
expires_date = int(time.time() / 3600) + EXPIRES_PERIOD_MONTH
now = 434385
flag = True


def create_rabbit_notification(user, transaction_id, expires_date=expires_date, now=now):
    time_diff = expires_date - now
    print("now =", now)
    print("time_diff =", time_diff)
    # 当时间差大于过期后两天时间 小于0, 则放入1小时一查询的队列
    if -2 * DELAY_DAY < time_diff < 0:
        global flag
        if flag:
            expires_date = cancel_renewed(expires_date)
            flag = False

        print("当时间差大于过期后两天时间 小于0, 则放入1小时一查询的队列")

        routing_key = "out.routing.key"
        request_exchange = "out.exchange.direct"
        expiration = str(DELAY_HOURS)

    # 当时间差小于一天时, 放入1小时一查询的队列
    elif 0 <= time_diff <= DELAY_DAY:
        print("当时间差小于一天时, 放入1小时一查询的队列")

        routing_key = "out.routing.key"
        request_exchange = "out.exchange.direct"
        expiration = str(DELAY_HOURS)

    # 当时间差小于七天时, 放入1天一查询的队列
    elif DELAY_DAY < time_diff <= 7 * DELAY_DAY:
        print("当时间差小于七天时, 放入1天一查询的队列")
        routing_key = "oneDay.routing.key"
        request_exchange = "oneDay.exchange.direct"
        expiration = str(DELAY_DAY)

    # 理论上不会出现这种情况
    elif 7 * DELAY_DAY < time_diff < 13 * DELAY_DAY:
        print("理论上不会出现这种情况")
        return

    # 当订阅时间为一年时, 在最后会出现还剩 14-15 的过期时间差, 将其放入一天一查询的队列
    elif 13 * DELAY_DAY <= time_diff <= 16 * DELAY_DAY:
        print("当订阅时间为一年时, 在最后会出现还剩 14-15 的过期时间差, 将其放入一天一查询的队列")

        routing_key = "oneDay.routing.key"
        request_exchange = "oneDay.exchange.direct"
        expiration = str(DELAY_DAY)

    # 当时间差大于七天小于27天时, 证明有同样的数据存在队列, 未处理, 放入27天一查询的队列
    elif 16 * DELAY_DAY < time_diff <= 27 * DELAY_DAY:
        print("当时间差大于七天小于27天时, 证明有同样的数据存在队列, 未处理, 放入27天一查询的队列")

        routing_key = "monthDay.routing.key"
        request_exchange = "monthDay.exchange.direct"
        expiration = str(DELAY_MONTH)

    # 当时间差大于27天时, 放入27天一查询的队列
    elif time_diff > 27 * DELAY_DAY:
        print("当时间差大于27天时, 放入27天一查询的队列")
        routing_key = "monthDay.routing.key"
        request_exchange = "monthDay.exchange.direct"
        expiration = str(DELAY_MONTH)

    # 当时间差小于-2天时, 视为续订失败
    else:
        print("Fail")
        return

    data = {"uid": user, "transaction_id": transaction_id, "expires_date": expires_date,
            "routing_key": routing_key, "request_exchange": request_exchange}

    mapping = {
        "out.routing.key": HoursNotification(),
        "oneDay.routing.key": DayNotification(),
        "monthDay.routing.key": mq_queue,
    }
    obj = mapping.get(routing_key)
    user = data["uid"]
    transaction_id = data["transaction_id"]
    print(data)
    obj.push(data)
    return data, routing_key


class BaseNotification:
    queue = []

    def push(self, value):
        self.queue.append(value)
        data, now = self.pop()
        user = data["uid"]
        transaction_id = data["transaction_id"]
        expires = data.get("expires_date")
        if expires:
            expires_date = expires
        create_rabbit_notification(user, transaction_id, expires_date, now)
        return self.queue

    def pop(self):
        global now
        print(self.num)
        time.sleep(5)
        now += self.num
        ret = self.queue.pop(0)
        return ret, now


class MonthNotification(BaseNotification):
    num = DELAY_MONTH


class DayNotification(BaseNotification):
    num = DELAY_DAY


class HoursNotification(BaseNotification):
    num = DELAY_HOURS


mq_queue = MonthNotification()
mapping = {
    "out.routing.key": HoursNotification(),
    "oneDay.routing.key": DayNotification(),
    "monthDay.routing.key": mq_queue,
}


def cancel_renewed(expires_date):
    expires_date += EXPIRES_PERIOD_MONTH
    return expires_date


create_rabbit_notification(1, "0001")
