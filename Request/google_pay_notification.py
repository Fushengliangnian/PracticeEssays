#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : lidong@immusician.com
# @Site    :
# @File    :

import requests
header = {
    "accept": "application/json",
    "content-type": "application/json",
    # "UID": "23",
    # "Token": "GOD"
}
data = {'message': {'data': '1eyJ2ZXJzaW9uIjoiMS4wIiwicGFja2FnZU5hbWUiOiJjb20ub2ttdXNpY2lhbi5hbmRyb2lkIiwiZXZlbnRUaW1lTWlsbGlzIjoiMTU2MjczOTY1NTA0NiIsInN1YnNjcmlwdGlvbk5vdGlmaWNhdGlvbiI6eyJ2ZXJzaW9uIjoiMS4wIiwibm90aWZpY2F0aW9uVHlwZSI6MiwicHVyY2hhc2VUb2tlbiI6InBjcGxna2RrZ2tmZGpqZHBlaWRlYWpqbS5BTy1KMU95ZDE3VVBJd2pQQWFpb1BCRHlYQTZfZVlYLVZ2TXNUSlNxM2RvdlZMb2JzM19NUVlMYW9XbzRmLWxkSUVVZ2tKRnpzQlhHTVZiQm1vSDVCdllNdndjNmFPLWxoVExfejJzckppWVRuX1prQnpEclM5WEFyQXBHTFhiemJYeUY4T2dKS1hJNXNnVlB5Ukw0bmVORWItVk8zRXZBWUEiLCJzdWJzY3JpcHRpb25JZCI6Im9rbXVzaWNpYW4ubW9udGhseS5ndWl0YXIifX0=', 'messageId': '676529954566470', 'message_id': '676529954566470', 'publishTime': '2019-07-10T06:20:55.622Z', 'publish_time': '2019-07-10T06:20:55.622Z'}, 'subscription': 'projects/evocative-radar-246211/subscriptions/sub_test_push'}

# 取消
# data = {'message': {'data': 'eyJ2ZXJzaW9uIjoiMS4wIiwicGFja2FnZU5hbWUiOiJjb20ub2ttdXNpY2lhbi5hbmRyb2lkIiwiZXZlbnRUaW1lTWlsbGlzIjoiMTU2MjczOTA4MzMzOCIsInN1YnNjcmlwdGlvbk5vdGlmaWNhdGlvbiI6eyJ2ZXJzaW9uIjoiMS4wIiwibm90aWZpY2F0aW9uVHlwZSI6MywicHVyY2hhc2VUb2tlbiI6Im9lY21sbW5mbWVqZ2Jham5sZnBpZXBkZC5BTy1KMU94RDZyQW9aWjFnbTlBNGdPMVBoZmhNOXhuZWJkVzc1ZjNtQ2FlZGgxcVg0LVk1NUxUZkZSekIxWml5WnZlaEdHV2U2aW5YcGwtaEo4d1NNLUVLM0ROR1VmbG1NWlFnbzloanVlZTQzY2R3c0FZMFAzaHJScmM3cXJyMGJVdGxETml2a0NYdyIsInN1YnNjcmlwdGlvbklkIjoib2ttdXNpY2lhbi55ZWFybHkuZ3VpdGFyIn19', 'messageId': '611287925672884', 'message_id': '611287925672884', 'publishTime': '2019-07-10T06:11:23.692Z', 'publish_time': '2019-07-10T06:11:23.692Z'}, 'subscription': 'projects/evocative-radar-246211/subscriptions/sub_test_push'}

data = {'message': {'data': 'eyJ2ZXJzaW9uIjoiMS4wIiwicGFja2FnZU5hbWUiOiJjb20ub2ttdXNpY2lhbi5hbmRyb2lkIiwiZXZlbnRUaW1lTWlsbGlzIjoiMTU2MjczOTAzNTEyOSIsInN1YnNjcmlwdGlvbk5vdGlmaWNhdGlvbiI6eyJ2ZXJzaW9uIjoiMS4wIiwibm90aWZpY2F0aW9uVHlwZSI6NCwicHVyY2hhc2VUb2tlbiI6Im9lY21sbW5mbWVqZ2Jham5sZnBpZXBkZC5BTy1KMU94RDZyQW9aWjFnbTlBNGdPMVBoZmhNOXhuZWJkVzc1ZjNtQ2FlZGgxcVg0LVk1NUxUZkZSekIxWml5WnZlaEdHV2U2aW5YcGwtaEo4d1NNLUVLM0ROR1VmbG1NWlFnbzloanVlZTQzY2R3c0FZMFAzaHJScmM3cXJyMGJVdGxETml2a0NYdyIsInN1YnNjcmlwdGlvbklkIjoib2ttdXNpY2lhbi55ZWFybHkuZ3VpdGFyIn19', 'messageId': '611283052513650', 'message_id': '611283052513650', 'publishTime': '2019-07-10T06:10:35.838Z', 'publish_time': '2019-07-10T06:10:35.838Z'}, 'subscription': 'projects/evocative-radar-246211/subscriptions/sub_test_push'}

ret = requests.post("http://127.0.0.1:8001/v9/subscription/google/notification/", headers=header, json=data)
print(ret.content)
print(ret.status_code)


# 正常订阅
decode_success_data = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562743877777', 'subscriptionNotification': {'version': '1.0', 'notificationType': 4, 'purchaseToken': 'inejlboacbpkmoidmfhccnia.AO-J1OzZK0EBe6jAxdjorbFpmLytZqb_msNKipdWUcXZkE6MJxMK7W5ps7t3NHQX-fop-_1CV38kAO7eE7nnBuX3k9vtVe98_UG4Qb7gXlV3pV57dsXN9u0g-_O_9uv649_CnEvigU7o0ShsZy1im_EC8FwHLlesPw', 'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info = {'error': 0, 'msg': 'OK', 'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562743876561', 'expiryTimeMillis': '1562744269081', 'autoRenewing': True, 'priceCurrencyCode': 'USD', 'priceAmountMicros': '9990000', 'countryCode': 'HK', 'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}', 'paymentState': 1, 'orderId': 'GPA.3381-0608-3667-73375', 'purchaseType': 0, 'acknowledgementState': 1}}


# 暂停订阅
decode_success_data_stop = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562743952680', 'subscriptionNotification': {'version': '1.0', 'notificationType': 11, 'purchaseToken': 'inejlboacbpkmoidmfhccnia.AO-J1OzZK0EBe6jAxdjorbFpmLytZqb_msNKipdWUcXZkE6MJxMK7W5ps7t3NHQX-fop-_1CV38kAO7eE7nnBuX3k9vtVe98_UG4Qb7gXlV3pV57dsXN9u0g-_O_9uv649_CnEvigU7o0ShsZy1im_EC8FwHLlesPw', 'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_stop = {'error': 0, 'msg': 'OK', 'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562743876561', 'expiryTimeMillis': '1562744269081', 'autoResumeTimeMillis': '1562744449081', 'autoRenewing': True, 'priceCurrencyCode': 'USD', 'priceAmountMicros': '9990000', 'countryCode': 'HK', 'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}', 'paymentState': 1, 'orderId': 'GPA.3381-0608-3667-73375', 'purchaseType': 0, 'acknowledgementState': 1}}


# 取消订阅
decode_success_data_cancel = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562744003843', 'subscriptionNotification': {'version': '1.0', 'notificationType': 3, 'purchaseToken': 'inejlboacbpkmoidmfhccnia.AO-J1OzZK0EBe6jAxdjorbFpmLytZqb_msNKipdWUcXZkE6MJxMK7W5ps7t3NHQX-fop-_1CV38kAO7eE7nnBuX3k9vtVe98_UG4Qb7gXlV3pV57dsXN9u0g-_O_9uv649_CnEvigU7o0ShsZy1im_EC8FwHLlesPw', 'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_cancel = {'error': 0, 'msg': 'OK', 'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562743876561', 'expiryTimeMillis': '1562744149081', 'autoRenewing': False, 'priceCurrencyCode': 'USD', 'priceAmountMicros': '9990000', 'countryCode': 'HK', 'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}', 'paymentState': 1, 'cancelReason': 0, 'userCancellationTimeMillis': '1562744003561', 'orderId': 'GPA.3381-0608-3667-73375', 'purchaseType': 0, 'acknowledgementState': 1}}

# 订阅过期后手动二次订阅
decode_success_data_2 = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562744584163', 'subscriptionNotification': {'version': '1.0', 'notificationType': 4, 'purchaseToken': 'mmfcececlgpoplggaiigbpij.AO-J1OyENLqSp6a7M2x0S4YHyfl3lBnRKs6VKZZ_qcDAPkdKUK9tPNIcUqyp9KBbCdtFMJ0nf3HFP1lq6Qxib-gSos-4bQ6jPjqDuP6VFgTA2kUVgZAOSedRlo2K3W-8TxWZfjtJm9sGPj526qmjg5CSDoI07IvwaA', 'subscriptionId': 'okmusician.monthly.guitar'}}


google_order_info_2 = {'error': 0, 'msg': 'OK', 'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562744583218', 'expiryTimeMillis': '1562744996153', 'autoRenewing': True, 'priceCurrencyCode': 'USD', 'priceAmountMicros': '9990000', 'countryCode': 'HK', 'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}', 'paymentState': 1, 'orderId': 'GPA.3373-4243-8326-81020', 'purchaseType': 0, 'acknowledgementState': 1}}

# 二次订阅之暂停订阅
decode_success_data_c2 = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562744769285', 'subscriptionNotification': {'version': '1.0', 'notificationType': 11, 'purchaseToken': 'mmfcececlgpoplggaiigbpij.AO-J1OyENLqSp6a7M2x0S4YHyfl3lBnRKs6VKZZ_qcDAPkdKUK9tPNIcUqyp9KBbCdtFMJ0nf3HFP1lq6Qxib-gSos-4bQ6jPjqDuP6VFgTA2kUVgZAOSedRlo2K3W-8TxWZfjtJm9sGPj526qmjg5CSDoI07IvwaA', 'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_c2 = {'error': 0, 'msg': 'OK', 'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562744583218', 'expiryTimeMillis': '1562744996153', 'autoResumeTimeMillis': '1562745176153', 'autoRenewing': True, 'priceCurrencyCode': 'USD', 'priceAmountMicros': '9990000', 'countryCode': 'HK', 'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}', 'paymentState': 1, 'orderId': 'GPA.3373-4243-8326-81020', 'purchaseType': 0, 'acknowledgementState': 1}}

# 二次订阅之恢复订阅
decode_success_data_r2 = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562744778074', 'subscriptionNotification': {'version': '1.0', 'notificationType': 11, 'purchaseToken': 'mmfcececlgpoplggaiigbpij.AO-J1OyENLqSp6a7M2x0S4YHyfl3lBnRKs6VKZZ_qcDAPkdKUK9tPNIcUqyp9KBbCdtFMJ0nf3HFP1lq6Qxib-gSos-4bQ6jPjqDuP6VFgTA2kUVgZAOSedRlo2K3W-8TxWZfjtJm9sGPj526qmjg5CSDoI07IvwaA', 'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_r2 = {'error': 0, 'msg': 'OK', 'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562744583218', 'expiryTimeMillis': '1562744996153', 'autoRenewing': True, 'priceCurrencyCode': 'USD', 'priceAmountMicros': '9990000', 'countryCode': 'HK', 'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}', 'paymentState': 1, 'orderId': 'GPA.3373-4243-8326-81020', 'purchaseType': 0, 'acknowledgementState': 1}}


decode_success_data_n2 = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562744880216', 'subscriptionNotification': {'version': '1.0', 'notificationType': 2, 'purchaseToken': 'mmfcececlgpoplggaiigbpij.AO-J1OyENLqSp6a7M2x0S4YHyfl3lBnRKs6VKZZ_qcDAPkdKUK9tPNIcUqyp9KBbCdtFMJ0nf3HFP1lq6Qxib-gSos-4bQ6jPjqDuP6VFgTA2kUVgZAOSedRlo2K3W-8TxWZfjtJm9sGPj526qmjg5CSDoI07IvwaA', 'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_n2 = {'error': 0, 'msg': 'OK', 'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562744583218', 'expiryTimeMillis': '1562745296153', 'autoRenewing': True, 'priceCurrencyCode': 'USD', 'priceAmountMicros': '9990000', 'countryCode': 'HK', 'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}', 'paymentState': 1, 'orderId': 'GPA.3373-4243-8326-81020..0', 'purchaseType': 0, 'acknowledgementState': 1}}


decode_success_data_nn2 = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562745180560', 'subscriptionNotification': {'version': '1.0', 'notificationType': 2, 'purchaseToken': 'mmfcececlgpoplggaiigbpij.AO-J1OyENLqSp6a7M2x0S4YHyfl3lBnRKs6VKZZ_qcDAPkdKUK9tPNIcUqyp9KBbCdtFMJ0nf3HFP1lq6Qxib-gSos-4bQ6jPjqDuP6VFgTA2kUVgZAOSedRlo2K3W-8TxWZfjtJm9sGPj526qmjg5CSDoI07IvwaA', 'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_nn2 = {'error': 0, 'msg': 'OK', 'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562744583218', 'expiryTimeMillis': '1562745596153', 'autoRenewing': True, 'priceCurrencyCode': 'USD', 'priceAmountMicros': '9990000', 'countryCode': 'HK', 'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}', 'paymentState': 1, 'orderId': 'GPA.3373-4243-8326-81020..1', 'purchaseType': 0, 'acknowledgementState': 1}}


decode_success_data_12m = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562746380354', 'subscriptionNotification': {'version': '1.0', 'notificationType': 2, 'purchaseToken': 'mmfcececlgpoplggaiigbpij.AO-J1OyENLqSp6a7M2x0S4YHyfl3lBnRKs6VKZZ_qcDAPkdKUK9tPNIcUqyp9KBbCdtFMJ0nf3HFP1lq6Qxib-gSos-4bQ6jPjqDuP6VFgTA2kUVgZAOSedRlo2K3W-8TxWZfjtJm9sGPj526qmjg5CSDoI07IvwaA', 'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_12m = {
    'kind': 'androidpublisher#subscriptionPurchase',
    'startTimeMillis': '1562744583218',
    'expiryTimeMillis': '1562746796153',
    'autoRenewing': True,
    'priceCurrencyCode': 'USD',
    'priceAmountMicros': '9990000',
    'countryCode': 'HK',
    'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}',
    'paymentState': 1,
    'orderId': 'GPA.3373-4243-8326-81020..5',
    'purchaseType': 0,
    'acknowledgementState': 1
}


decode_success_data_17m = {'version': '1.0', 'packageName': 'com.okmusician.android', 'eventTimeMillis': '1562746678937', 'subscriptionNotification': {'version': '1.0', 'notificationType': 3, 'purchaseToken': 'mmfcececlgpoplggaiigbpij.AO-J1OyENLqSp6a7M2x0S4YHyfl3lBnRKs6VKZZ_qcDAPkdKUK9tPNIcUqyp9KBbCdtFMJ0nf3HFP1lq6Qxib-gSos-4bQ6jPjqDuP6VFgTA2kUVgZAOSedRlo2K3W-8TxWZfjtJm9sGPj526qmjg5CSDoI07IvwaA', 'subscriptionId': 'okmusician.monthly.guitar'}}

google_order_info_17m = {'error': 0, 'msg': 'OK', 'data': {'kind': 'androidpublisher#subscriptionPurchase', 'startTimeMillis': '1562744583218', 'expiryTimeMillis': '1562746676153', 'autoRenewing': False, 'priceCurrencyCode': 'USD', 'priceAmountMicros': '9990000', 'countryCode': 'HK', 'developerPayload': '{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}', 'cancelReason': 1, 'orderId': 'GPA.3373-4243-8326-81020..5', 'purchaseType': 0, 'acknowledgementState': 1}}