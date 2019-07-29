#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : lidong@immusician.com
# @Site    :
# @File    :

# 订阅
decode_success_data = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562810957722',
                       'subscriptionNotification': {'version': '1.0', 'notificationType': 4,
                                                    'purchaseToken': 'pelghecgioenpdmbngnoinhl.AO-J1OywoQ2SPNnGWDJRxYh_f8pBlidM3hAEjNuBoodTIrI-n9Awi7kc57CQRQP1WJgDTCTZs3x_cZhCAk33sVyY1fhDUM09H5iuvxaALZCKY3OtJwXBHZ5k19R46172_1O103_sg-k82bU-UzZRldlvafWibVPYOw',
                                                    'subscriptionId': 'okmusician.yearly.ukulele'}}

google_order_info = {'error': 0, 'msg': 'OK',
                     'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562810956378',
                              'expiryTimeMillis': '1562812850305', 'autoRenewing': True, 'priceCurrencyCode': 'USD',
                              'priceAmountMicros': '49990000', 'countryCode': 'HK',
                              'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}',
                              'paymentState': 1, 'orderId': 'GPA.3367-3497-6248-17668', 'purchaseType': 0,
                              'acknowledgementState': 1}}

# 暂停订阅 yearly 无暂停按钮 只有取消
decode_success_data_c = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562811259368',
                         'subscriptionNotification': {'version': '1.0', 'notificationType': 3,
                                                      'purchaseToken': 'pelghecgioenpdmbngnoinhl.AO-J1OywoQ2SPNnGWDJRxYh_f8pBlidM3hAEjNuBoodTIrI-n9Awi7kc57CQRQP1WJgDTCTZs3x_cZhCAk33sVyY1fhDUM09H5iuvxaALZCKY3OtJwXBHZ5k19R46172_1O103_sg-k82bU-UzZRldlvafWibVPYOw',
                                                      'subscriptionId': 'okmusician.yearly.ukulele'}}

google_order_info_c = {'error': 0, 'msg': 'OK',
                       'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562810956378',
                                'expiryTimeMillis': '1562812730305', 'autoRenewing': False, 'priceCurrencyCode': 'USD',
                                'priceAmountMicros': '49990000', 'countryCode': 'HK',
                                'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}',
                                'paymentState': 1, 'cancelReason': 0, 'userCancellationTimeMillis': '1562811259120',
                                'orderId': 'GPA.3367-3497-6248-17668', 'purchaseType': 0, 'acknowledgementState': 1}}

# 恢复
decode_success_data_r = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562811340486',
                         'subscriptionNotification': {'version': '1.0', 'notificationType': 7,
                                                      'purchaseToken': 'pelghecgioenpdmbngnoinhl.AO-J1OywoQ2SPNnGWDJRxYh_f8pBlidM3hAEjNuBoodTIrI-n9Awi7kc57CQRQP1WJgDTCTZs3x_cZhCAk33sVyY1fhDUM09H5iuvxaALZCKY3OtJwXBHZ5k19R46172_1O103_sg-k82bU-UzZRldlvafWibVPYOw',
                                                      'subscriptionId': 'okmusician.yearly.ukulele'}}

google_order_info_r = {'error': 0, 'msg': 'OK',
                       'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562810956378',
                                'expiryTimeMillis': '1562812850305', 'autoRenewing': True, 'priceCurrencyCode': 'USD',
                                'priceAmountMicros': '49990000', 'countryCode': 'HK',
                                'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}',
                                'paymentState': 1, 'orderId': 'GPA.3367-3497-6248-17668', 'purchaseType': 0,
                                'acknowledgementState': 1}}

# 第二次订阅
decode_success_data_2 = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562813391121',
                         'subscriptionNotification': {'version': '1.0', 'notificationType': 4,
                                                      'purchaseToken': 'mekakfoonkmfiihnfnppiibg.AO-J1Oy2ygqLxVJnmrskKWn9Zn5pb5LN6s1iHcBaK59O6kW5MhkuvgFnEgEwqoiEJOaBaYVbY6NPHxoTUlSXraysQET6P5EGHqvFuPIMzgP9ZW9BJX0YSnAWw3lg58uvXydE_xBCU2-drkXZYorrQmWGoc1N_v18VQ',
                                                      'subscriptionId': 'okmusician.monthly.ukulele'}}

google_order_info_2 = {'error': 0, 'msg': 'OK',
                       'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562813389196',
                                'expiryTimeMillis': '1562813796411', 'autoRenewing': True, 'priceCurrencyCode': 'USD',
                                'priceAmountMicros': '9990000', 'countryCode': 'HK',
                                'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}',
                                'paymentState': 1, 'orderId': 'GPA.3392-8863-7420-64123', 'purchaseType': 0,
                                'acknowledgementState': 1}}

# 暂停
decode_success_data_2_p = {'version': '1.0', 'packageName': 'com.okmusician.android',
                           'eventTimeMillis': '1562813482242',
                           'subscriptionNotification': {'version': '1.0', 'notificationType': 11,
                                                        'purchaseToken': 'mekakfoonkmfiihnfnppiibg.AO-J1Oy2ygqLxVJnmrskKWn9Zn5pb5LN6s1iHcBaK59O6kW5MhkuvgFnEgEwqoiEJOaBaYVbY6NPHxoTUlSXraysQET6P5EGHqvFuPIMzgP9ZW9BJX0YSnAWw3lg58uvXydE_xBCU2-drkXZYorrQmWGoc1N_v18VQ',
                                                        'subscriptionId': 'okmusician.monthly.ukulele'}}

google_order_info_2_p = {'error': 0, 'msg': 'OK',
                         'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562813389196',
                                  'expiryTimeMillis': '1562813796411', 'autoResumeTimeMillis': '1562814576411',
                                  'autoRenewing': True, 'priceCurrencyCode': 'USD', 'priceAmountMicros': '9990000',
                                  'countryCode': 'HK',
                                  'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}',
                                  'paymentState': 1, 'orderId': 'GPA.3392-8863-7420-64123', 'purchaseType': 0,
                                  'acknowledgementState': 1}}

# 恢复
decode_success_data_2_r = {'version': '1.0', 'packageName': 'com.okmusician.android',
                           'eventTimeMillis': '1562814585644',
                           'subscriptionNotification': {'version': '1.0', 'notificationType': 1,
                                                        'purchaseToken': 'mekakfoonkmfiihnfnppiibg.AO-J1Oy2ygqLxVJnmrskKWn9Zn5pb5LN6s1iHcBaK59O6kW5MhkuvgFnEgEwqoiEJOaBaYVbY6NPHxoTUlSXraysQET6P5EGHqvFuPIMzgP9ZW9BJX0YSnAWw3lg58uvXydE_xBCU2-drkXZYorrQmWGoc1N_v18VQ',
                                                        'subscriptionId': 'okmusician.monthly.ukulele'}}

google_order_info_2_r = {'error': 0, 'msg': 'OK',
                         'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562813389196',
                                  'expiryTimeMillis': '1562815004931', 'autoRenewing': True, 'priceCurrencyCode': 'USD',
                                  'priceAmountMicros': '9990000', 'countryCode': 'HK',
                                  'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}',
                                  'paymentState': 1, 'orderId': 'GPA.3392-8863-7420-64123..0', 'purchaseType': 0,
                                  'acknowledgementState': 1}}

# 续订
decode_success_data_2_rr = {'version': '1.0', 'packageName': 'com.okmusician.android',
                            'eventTimeMillis': '1562815190682',
                            'subscriptionNotification': {'version': '1.0', 'notificationType': 2,
                                                         'purchaseToken': 'mekakfoonkmfiihnfnppiibg.AO-J1Oy2ygqLxVJnmrskKWn9Zn5pb5LN6s1iHcBaK59O6kW5MhkuvgFnEgEwqoiEJOaBaYVbY6NPHxoTUlSXraysQET6P5EGHqvFuPIMzgP9ZW9BJX0YSnAWw3lg58uvXydE_xBCU2-drkXZYorrQmWGoc1N_v18VQ',
                                                         'subscriptionId': 'okmusician.monthly.ukulele'}}

google_order_info_2_rr = {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562813389196',
                          'expiryTimeMillis': '1562815604931', 'autoRenewing': True, 'priceCurrencyCode': 'USD',
                          'priceAmountMicros': '9990000', 'countryCode': 'HK',
                          'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}',
                          'paymentState': 1, 'orderId': 'GPA.3392-8863-7420-64123..2', 'purchaseType': 0,
                          'acknowledgementState': 1}

# 第三次订阅
decode_success_data_3 = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562824606064',
                         'subscriptionNotification': {'version': '1.0', 'notificationType': 4,
                                                      'purchaseToken': 'dfpemeldpjbhegjodfomhgko.AO-J1OxucWqfYBUN8g7ps0oDU4DcMG1GIATQ02yT41BF1wIm9BocYFTYFImhkfqWzss5zHuK3GpaQnD-JXHS3SWvAW4aOFVStwpsTKXNIzABSGu7Ic9rB_PPxytejt74pui7JKChlQ730qMzOY4XsfW3FbFRYX8b0g',
                                                      'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_3 = {'error': 0, 'msg': 'OK',
                       'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562824604079',
                                'expiryTimeMillis': '1562825013589', 'autoRenewing': True, 'priceCurrencyCode': 'USD',
                                'priceAmountMicros': '9990000', 'countryCode': 'HK',
                                'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}',
                                'paymentState': 1, 'orderId': 'GPA.3383-5743-3138-22882', 'purchaseType': 0,
                                'acknowledgementState': 1}}

# 暂停
decode_success_data_3_p = {'version': '1.0', 'packageName': 'com.okmusician.android',
                           'eventTimeMillis': '1562824779807',
                           'subscriptionNotification': {'version': '1.0', 'notificationType': 11,
                                                        'purchaseToken': 'dfpemeldpjbhegjodfomhgko.AO-J1OxucWqfYBUN8g7ps0oDU4DcMG1GIATQ02yT41BF1wIm9BocYFTYFImhkfqWzss5zHuK3GpaQnD-JXHS3SWvAW4aOFVStwpsTKXNIzABSGu7Ic9rB_PPxytejt74pui7JKChlQ730qMzOY4XsfW3FbFRYX8b0g',
                                                        'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_3_p = {'error': 0, 'msg': 'OK',
                         'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562824604079',
                                  'expiryTimeMillis': '1562825013589', 'autoResumeTimeMillis': '1562825493589',
                                  'autoRenewing': True, 'priceCurrencyCode': 'USD', 'priceAmountMicros': '9990000',
                                  'countryCode': 'HK',
                                  'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}',
                                  'paymentState': 1, 'orderId': 'GPA.3383-5743-3138-22882', 'purchaseType': 0,
                                  'acknowledgementState': 1}}

# 恢复
# 恢复发了两条 一条 未知10 一条恢复1
decode_success_data_3_r = {'version': '1.0', 'packageName': 'com.okmusician.android',
                           'eventTimeMillis': '1562824895956',
                           'subscriptionNotification': {'version': '1.0', 'notificationType': 10,
                                                        'purchaseToken': 'dfpemeldpjbhegjodfomhgko.AO-J1OxucWqfYBUN8g7ps0oDU4DcMG1GIATQ02yT41BF1wIm9BocYFTYFImhkfqWzss5zHuK3GpaQnD-JXHS3SWvAW4aOFVStwpsTKXNIzABSGu7Ic9rB_PPxytejt74pui7JKChlQ730qMzOY4XsfW3FbFRYX8b0g',
                                                        'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_3_r = {'error': 0, 'msg': 'OK',
                         'data': {'kind': 'androidpublisher#subscriptionPurchase',
                                  'startTimeMillis': '1562824604079',
                                  'expiryTimeMillis': '1562824893589',
                                  'autoResumeTimeMillis': '1562825493589',
                                  'autoRenewing': True,
                                  'priceCurrencyCode': 'USD',
                                  'priceAmountMicros': '9990000',
                                  'countryCode': 'HK',
                                  'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}',
                                  'paymentState': 1,
                                  'orderId': 'GPA.3383-5743-3138-22882',
                                  'purchaseType': 0,
                                  'acknowledgementState': 1}}

decode_success_data_3_n = {'version': '1.0', 'packageName': 'com.okmusician.android',
                           'eventTimeMillis': '1562824921731',
                           'subscriptionNotification': {'version': '1.0', 'notificationType': 1,
                                                        'purchaseToken': 'dfpemeldpjbhegjodfomhgko.AO-J1OxucWqfYBUN8g7ps0oDU4DcMG1GIATQ02yT41BF1wIm9BocYFTYFImhkfqWzss5zHuK3GpaQnD-JXHS3SWvAW4aOFVStwpsTKXNIzABSGu7Ic9rB_PPxytejt74pui7JKChlQ730qMzOY4XsfW3FbFRYX8b0g',
                                                        'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_3_n = {'error': 0, 'msg': 'OK',
                         'data': {'kind': 'androidpublisher#subscriptionPurchase',
                                  'startTimeMillis': '1562824604079',
                                  'expiryTimeMillis': '1562825340763',
                                  'autoRenewing': True,
                                  'priceCurrencyCode': 'USD',
                                  'priceAmountMicros': '9990000',
                                  'countryCode': 'HK',
                                  'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}',
                                  'paymentState': 1,
                                  'orderId': 'GPA.3383-5743-3138-22882..0',
                                  'purchaseType': 0,
                                  'acknowledgementState': 1}}

############################### 提测 ###############################
decode_success_data_4 = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562828926678',
                         'subscriptionNotification': {'version': '1.0', 'notificationType': 4,
                                                      'purchaseToken': 'amoccidenkficdofbcklpioh.AO-J1OxxYdrev1uZh6ZCgg7FcQZJL1uDA7Z1hiPwW8tdxC3d9Cpzoq0vcfrkJ6oTMNtTFxcsZezREYh7vfP2MB2HcOAjW7Zjvyh-i8BuxFyGuFRdKiMOalTEf95A01Fe3GFPVvP2fpaz1iDx5j8ACQhYkhuvMhybhA',
                                                      'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_4 = {'error': 0, 'msg': 'OK',
                       'data': {'kind': 'androidpublisher#subscriptionPurchase',
                                'startTimeMillis': '1562828925262',
                                'expiryTimeMillis': '1562829638317',
                                'autoRenewing': True,
                                'priceCurrencyCode': 'USD',
                                'priceAmountMicros': '9990000',
                                'countryCode': 'HK',
                                'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}',
                                'paymentState': 1,
                                'orderId': 'GPA.3310-6696-8939-00792..0',
                                'purchaseType': 0,
                                'acknowledgementState': 1}}

decode_success_data_4_r = {'version': '1.0', 'packageName': 'com.okmusician.android',
                           'eventTimeMillis': '1562829523362',
                           'subscriptionNotification': {'version': '1.0', 'notificationType': 2,
                                                        'purchaseToken': 'amoccidenkficdofbcklpioh.AO-J1OxxYdrev1uZh6ZCgg7FcQZJL1uDA7Z1hiPwW8tdxC3d9Cpzoq0vcfrkJ6oTMNtTFxcsZezREYh7vfP2MB2HcOAjW7Zjvyh-i8BuxFyGuFRdKiMOalTEf95A01Fe3GFPVvP2fpaz1iDx5j8ACQhYkhuvMhybhA',
                                                        'subscriptionId': 'okmusician.monthly.guitar'}}

# 第五次
decode_success_data_5 = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562831022608',
                         'subscriptionNotification': {'version': '1.0', 'notificationType': 4,
                                                      'purchaseToken': 'nfcocmmnijldkcfgpnamcgkl.AO-J1OxEukEYS7xXGdVyyjOeevZ3ZG7qo2QYGy_EPysR-hgTGO9wZtvLn6Ly47DOp1Rfx9R3kwz8XxS5qXnUc5Ep7tw6wk3oF08EEWJa2bb4BgPirAFllx8TCeQ20lxgmvJINC1SMw44HSCRNS3ghRfjHxVUf7pp_w',
                                                      'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_5 = {'error': 0, 'msg': 'OK',
                       'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562831020709',
                                'expiryTimeMillis': '1562831433803', 'autoRenewing': True, 'priceCurrencyCode': 'USD',
                                'priceAmountMicros': '9990000', 'countryCode': 'HK',
                                'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}',
                                'paymentState': 1, 'orderId': 'GPA.3338-9934-5132-43720', 'purchaseType': 0,
                                'acknowledgementState': 1}}

# 第六次
decode_success_data_6 = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562833620690',
                         'subscriptionNotification': {'version': '1.0', 'notificationType': 4,
                                                      'purchaseToken': 'mkdadjgeobfegabkmkppcncj.AO-J1OzM9SUlUjaqQpZTNf44u8o0dCkL1kL9_53lquBFPBTV4v3V2w328X7Jg2FMNHyxoiDls8UHnNzijyiKmAZzynk0v5j4VJQKPf9-Me57LWoifIl34jrjrvso14S8c81CZuki1atISYFpmBNT1IVDRV9c_BBqfA',
                                                      'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_6 = {'error': 0, 'msg': 'OK',
                       'data': {'kind': 'androidpublisher#subscriptionPurchase',
                                'startTimeMillis': '1562833619592',
                                'expiryTimeMillis': '1562834030052',
                                'autoRenewing': True,
                                'priceCurrencyCode': 'USD',
                                'priceAmountMicros': '9990000',
                                'countryCode': 'HK',
                                'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}',
                                'paymentState': 1,
                                'orderId': 'GPA.3394-5074-3617-09146',
                                'purchaseType': 0,
                                'acknowledgementState': 1}}

# 1562836879634
# 1562837179634
#
# 4 ——> 11
# 5 ——> 2/1
# 6: 42
#
#
# 续:  7:44
# 暂:  7:44 - 7: 49
#
# 8: 27
#
# 32   自动恢复 ——> 1
#
# 37 - 42
#
# 46
#
# 9: 14
