#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : lidong@immusician.com
# @Site    :
# @File    :

uid = 452

# 第一次订阅
decode_success_data = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562765824850',
                       'subscriptionNotification': {'version': '1.0', 'notificationType': 4,
                                                    'purchaseToken': 'dlialmpjmneecoodokhoonmj.AO-J1OzFBOxbT7Zf9YbQD4PYcLgoChX0Bldgyq_sHyFyYBriNNqMQ5WyfwI7YJdhUWYNn2-ne3BddBwZi3fvYO6LzngDYC4kIEqMmOwX-qmnHXc-vFn9x_SjtoWjHrhqqFTKTWngXU37yGhw16b0kzRSsvX0XPB32g',
                                                    'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info = {'error': 0, 'msg': 'OK',
                     'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562765822781',
                              'expiryTimeMillis': '1562766235994', 'autoRenewing': True, 'priceCurrencyCode': 'USD',
                              'priceAmountMicros': '9990000', 'countryCode': 'HK',
                              'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}',
                              'paymentState': 1, 'orderId': 'GPA.3302-8932-6921-28459', 'purchaseType': 0,
                              'acknowledgementState': 1}}

# 第一次续订
decode_success_data_r1 = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562766123060',
                          'subscriptionNotification': {'version': '1.0', 'notificationType': 2,
                                                       'purchaseToken': 'dlialmpjmneecoodokhoonmj.AO-J1OzFBOxbT7Zf9YbQD4PYcLgoChX0Bldgyq_sHyFyYBriNNqMQ5WyfwI7YJdhUWYNn2-ne3BddBwZi3fvYO6LzngDYC4kIEqMmOwX-qmnHXc-vFn9x_SjtoWjHrhqqFTKTWngXU37yGhw16b0kzRSsvX0XPB32g',
                                                       'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_r1 = {'error': 0, 'msg': 'OK',
                        'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562765822781',
                                 'expiryTimeMillis': '1562766535994', 'autoRenewing': True, 'priceCurrencyCode': 'USD',
                                 'priceAmountMicros': '9990000', 'countryCode': 'HK',
                                 'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}',
                                 'paymentState': 1, 'orderId': 'GPA.3302-8932-6921-28459..0', 'purchaseType': 0,
                                 'acknowledgementState': 1,
                                 'purchaseToken': 'dlialmpjmneecoodokhoonmj.AO-J1OzFBOxbT7Zf9YbQD4PYcLgoChX0Bldgyq_sHyFyYBriNNqMQ5WyfwI7YJdhUWYNn2-ne3BddBwZi3fvYO6LzngDYC4kIEqMmOwX-qmnHXc-vFn9x_SjtoWjHrhqqFTKTWngXU37yGhw16b0kzRSsvX0XPB32g'}}

# 第二次
decode_success_data_r2 = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562766426079',
                          'subscriptionNotification': {'version': '1.0', 'notificationType': 2,
                                                       'purchaseToken': 'dlialmpjmneecoodokhoonmj.AO-J1OzFBOxbT7Zf9YbQD4PYcLgoChX0Bldgyq_sHyFyYBriNNqMQ5WyfwI7YJdhUWYNn2-ne3BddBwZi3fvYO6LzngDYC4kIEqMmOwX-qmnHXc-vFn9x_SjtoWjHrhqqFTKTWngXU37yGhw16b0kzRSsvX0XPB32g',
                                                       'subscriptionId': 'okmusician.monthly.guitar'}}


############################################################


# 第二次订阅
decode_success_data_2 = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562767215805', 'subscriptionNotification': {'version': '1.0', 'notificationType': 4, 'purchaseToken': 'laeggmnjjjejoemfmcclooib.AO-J1Oxvir-1a8MtW2n8BsRAJ-u04Q0WVa1DfXoFtjeAhzqmPvvqP1heN8QRtvZyt-FoGLCLQNZE30AcZxgCa_GwlMrOBgJDDcyI9xVl4OAUvlZLd0ENkPEyGmXWEKR9KhaOObK7_PT0trBUM6tUatR9tDg3gw1Sow', 'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_2 = {'error': 0, 'msg': 'OK', 'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562767214588', 'expiryTimeMillis': '1562767626493', 'autoRenewing': True, 'priceCurrencyCode': 'USD', 'priceAmountMicros': '9990000', 'countryCode': 'HK', 'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}', 'paymentState': 1, 'orderId': 'GPA.3310-1531-5141-42956', 'purchaseType': 0, 'acknowledgementState': 1}}


# 第二次订阅第一次续订
decode_success_data_2_r1 = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562767518963', 'subscriptionNotification': {'version': '1.0', 'notificationType': 2, 'purchaseToken': 'laeggmnjjjejoemfmcclooib.AO-J1Oxvir-1a8MtW2n8BsRAJ-u04Q0WVa1DfXoFtjeAhzqmPvvqP1heN8QRtvZyt-FoGLCLQNZE30AcZxgCa_GwlMrOBgJDDcyI9xVl4OAUvlZLd0ENkPEyGmXWEKR9KhaOObK7_PT0trBUM6tUatR9tDg3gw1Sow', 'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_2_r1 = {'error': 0, 'msg': 'OK', 'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562767214588', 'expiryTimeMillis': '1562767926493', 'autoRenewing': True, 'priceCurrencyCode': 'USD', 'priceAmountMicros': '9990000', 'countryCode': 'HK', 'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}', 'paymentState': 1, 'orderId': 'GPA.3310-1531-5141-42956..0', 'purchaseType': 0, 'acknowledgementState': 1, 'purchaseToken': 'laeggmnjjjejoemfmcclooib.AO-J1Oxvir-1a8MtW2n8BsRAJ-u04Q0WVa1DfXoFtjeAhzqmPvvqP1heN8QRtvZyt-FoGLCLQNZE30AcZxgCa_GwlMrOBgJDDcyI9xVl4OAUvlZLd0ENkPEyGmXWEKR9KhaOObK7_PT0trBUM6tUatR9tDg3gw1Sow'}}


# 第二次订阅第二次续订
decode_success_data_2_r2 = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562767811788', 'subscriptionNotification': {'version': '1.0', 'notificationType': 2, 'purchaseToken': 'laeggmnjjjejoemfmcclooib.AO-J1Oxvir-1a8MtW2n8BsRAJ-u04Q0WVa1DfXoFtjeAhzqmPvvqP1heN8QRtvZyt-FoGLCLQNZE30AcZxgCa_GwlMrOBgJDDcyI9xVl4OAUvlZLd0ENkPEyGmXWEKR9KhaOObK7_PT0trBUM6tUatR9tDg3gw1Sow', 'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_2_r2 = {'error': 0, 'msg': 'OK', 'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562767214588', 'expiryTimeMillis': '1562768226493', 'autoRenewing': True, 'priceCurrencyCode': 'USD', 'priceAmountMicros': '9990000', 'countryCode': 'HK', 'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}', 'paymentState': 1, 'orderId': 'GPA.3310-1531-5141-42956..1', 'purchaseType': 0, 'acknowledgementState': 1, 'purchaseToken': 'laeggmnjjjejoemfmcclooib.AO-J1Oxvir-1a8MtW2n8BsRAJ-u04Q0WVa1DfXoFtjeAhzqmPvvqP1heN8QRtvZyt-FoGLCLQNZE30AcZxgCa_GwlMrOBgJDDcyI9xVl4OAUvlZLd0ENkPEyGmXWEKR9KhaOObK7_PT0trBUM6tUatR9tDg3gw1Sow'}}


# 第二次订阅第三次续订
decode_success_data_2_r3 = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562768110438', 'subscriptionNotification': {'version': '1.0', 'notificationType': 2, 'purchaseToken': 'laeggmnjjjejoemfmcclooib.AO-J1Oxvir-1a8MtW2n8BsRAJ-u04Q0WVa1DfXoFtjeAhzqmPvvqP1heN8QRtvZyt-FoGLCLQNZE30AcZxgCa_GwlMrOBgJDDcyI9xVl4OAUvlZLd0ENkPEyGmXWEKR9KhaOObK7_PT0trBUM6tUatR9tDg3gw1Sow', 'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_2_r3 = {'error': 0, 'msg': 'OK', 'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562767214588', 'expiryTimeMillis': '1562768526493', 'autoRenewing': True, 'priceCurrencyCode': 'USD', 'priceAmountMicros': '9990000', 'countryCode': 'HK', 'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}', 'paymentState': 1, 'orderId': 'GPA.3310-1531-5141-42956..2', 'purchaseType': 0, 'acknowledgementState': 1, 'purchaseToken': 'laeggmnjjjejoemfmcclooib.AO-J1Oxvir-1a8MtW2n8BsRAJ-u04Q0WVa1DfXoFtjeAhzqmPvvqP1heN8QRtvZyt-FoGLCLQNZE30AcZxgCa_GwlMrOBgJDDcyI9xVl4OAUvlZLd0ENkPEyGmXWEKR9KhaOObK7_PT0trBUM6tUatR9tDg3gw1Sow'}}


# 第二次订阅第四次续订
# find db
item_log = {
    "_id" : ("5d25f41e0a10062b1ea9f965"),
    "orderId" : "GPA.3310-1531-5141-42956..3",
    "subscriber" : 452,
    "acknowledgementState" : "1",
    "autoRenewing" : True,
    "cancelReason" : None,
    "countryCode" : "HK",
    "developerPayload" : "{\"developerPayload\":\"\",\"is_free_trial\":false,\"has_introductory_price_trial\":false,\"is_updated\":false}",
    "expires_date" : "2019-07-10T14:27:06.493Z",
    "expiryTimeMillis" : 1562768826493,
    "is_delete" : False,
    "kind" : "androidpublisher#subscriptionPurchase",
    "linkedPurchaseToken" : None,
    "packageName" : "com.okmusician.android",
    "paymentState" : 1,
    "priceAmountMicros" : "9990000",
    "priceCurrencyCode" : "USD",
    "product_id" : "okmusician.monthly.guitar",
    "purchaseState" : 0,
    "purchaseTime" : (1562767214588),
    "purchaseToken" : "laeggmnjjjejoemfmcclooib.AO-J1Oxvir-1a8MtW2n8BsRAJ-u04Q0WVa1DfXoFtjeAhzqmPvvqP1heN8QRtvZyt-FoGLCLQNZE30AcZxgCa_GwlMrOBgJDDcyI9xVl4OAUvlZLd0ENkPEyGmXWEKR9KhaOObK7_PT0trBUM6tUatR9tDg3gw1Sow",
    "purchaseType" : 0,
    "startTimeMillis" : (1562767214588),
    "updated_at" : ("2019-07-10T14:00:19.339Z"),
    "userCancellationTimeMillis" : None
}
sub_main = {
    "_id" : 452,
    "acknowledgementState" : "1",
    "autoRenewing" : true,
    "cancelReason" : null,
    "countryCode" : "HK",
    "created_at" : ISODate("2019-07-10T06:46:54.533Z"),
    "developerPayload" : "{\"developerPayload\":\"\",\"is_free_trial\":false,\"has_introductory_price_trial\":false,\"is_updated\":false}",
    "expires_date" : ISODate("2019-07-10T14:27:06.493Z"),
    "expiryTimeMillis" : NumberLong(1562768826493),
    "is_delete" : false,
    "kind" : "androidpublisher#subscriptionPurchase",
    "linkedPurchaseToken" : null,
    "orderId" : "GPA.3310-1531-5141-42956..3",
    "packageName" : "com.okmusician.android",
    "paymentState" : 1,
    "priceAmountMicros" : "9990000",
    "priceCurrencyCode" : "USD",
    "product_id" : "okmusician.monthly.guitar",
    "purchaseState" : 0,
    "purchaseTime" : NumberLong(1562767214588),
    "purchaseToken" : "laeggmnjjjejoemfmcclooib.AO-J1Oxvir-1a8MtW2n8BsRAJ-u04Q0WVa1DfXoFtjeAhzqmPvvqP1heN8QRtvZyt-FoGLCLQNZE30AcZxgCa_GwlMrOBgJDDcyI9xVl4OAUvlZLd0ENkPEyGmXWEKR9KhaOObK7_PT0trBUM6tUatR9tDg3gw1Sow",
    "purchaseType" : 0,
    "startTimeMillis" : NumberLong(1562767214588),
    "subscriber" : 452,
    "updated_at" : ISODate("2019-07-10T14:00:19.339Z"),
    "userCancellationTimeMillis" : null
}


# 第二次订阅第五次续订
item_log_5 = {
    "_id": "5d25f54e0a10062b1ea9fb99",
    "subscriber": 452,
    "expiryTimeMillis": 1562769126493,
    "orderId": "GPA.3310-1531-5141-42956..4",

}
sub_main_5 = {
    "_id" : 452,
    "expiryTimeMillis" : 1562769126493,
    "orderId" : "GPA.3310-1531-5141-42956..4",
}


# 第二次订阅第六次续订
item_log_6 = {
    "_id": "5d25f6770a10062b1ea9fd81",
    "subscriber": 452,
    "expiryTimeMillis": 1562769426493,
    "orderId": "GPA.3310-1531-5141-42956..5",

}
sub_main_6 = {
    "_id" : 452,
    "expiryTimeMillis" : 1562769426493,
    "orderId" : "GPA.3310-1531-5141-42956..5",
}


# 第二次订阅第7次续订  失败
item_log_7 = {
    "_id": "5d25f6770a10062b1ea9fd81",
    "subscriber": 452,
    "expiryTimeMillis": 1562769426493,
    "orderId": "GPA.3310-1531-5141-42956..5",

}
sub_main_7 = {
    "_id" : 452,
    "expiryTimeMillis" : 1562769426493,
    "orderId" : "GPA.3310-1531-5141-42956..5",
}


