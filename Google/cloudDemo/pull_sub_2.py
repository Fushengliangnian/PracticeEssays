# import time
#
# from google.cloud import pubsub_v1
#
# project_id = "projects/evocative-radar-246211/topics/pay-notification"
# subscription_name = "projects/evocative-radar-246211/subscriptions/sub_test"
# cer_path = "/Users/mac/Downloads/service-account.json"
#
# subscriber = pubsub_v1.SubscriberClient.from_service_account_json(cer_path)
# subscription_path = subscriber.subscription_path(
#     project_id, subscription_name)
#
#
# def callback(message):
#     print('Received message: {}'.format(message.data))
#     if message.attributes:
#         print('Attributes:')
#         for key in message.attributes:
#             value = message.attributes.get(key)
#             print('{}: {}'.format(key, value))
#     message.ack()
#
#
# subscriber.subscribe(subscription_path, callback=callback)
#
# # The subscriber is non-blocking, so we must keep the main thread from
# # exiting to allow it to process messages in the background.
# print('Listening for messages on {}'.format(subscription_path))
# while True:
#     time.sleep(60)

import base64, json

# ret = {'message': {
#     'data': 'eyJ2ZXJzaW9uIjoiMS4wIiwicGFja2FnZU5hbWUiOiJjb20ub2ttdXNpY2lhbi5hbmRyb2lkIiwiZXZlbnRUaW1lTWlsbGlzIjoiMTU2MjczODAyOTQ5OSIsInRlc3ROb3RpZmljYXRpb24iOnsidmVyc2lvbiI6IjEuMCJ9fQ==',
#     'messageId': '611277014847514', 'message_id': '611277014847514', 'publishTime': '2019-07-10T05:53:49.543Z',
#     'publish_time': '2019-07-10T05:53:49.543Z'},
#        'subscription': 'projects/evocative-radar-246211/subscriptions/sub_test_push'}

# 正常订阅
ret = {'message': {'data': 'eyJ2ZXJzaW9uIjoiMS4wIiwicGFja2FnZU5hbWUiOiJjb20ub2ttdXNpY2lhbi5hbmRyb2lkIiwiZXZlbnRUaW1lTWlsbGlzIjoiMTU2MjczOTAzNTEyOSIsInN1YnNjcmlwdGlvbk5vdGlmaWNhdGlvbiI6eyJ2ZXJzaW9uIjoiMS4wIiwibm90aWZpY2F0aW9uVHlwZSI6NCwicHVyY2hhc2VUb2tlbiI6Im9lY21sbW5mbWVqZ2Jham5sZnBpZXBkZC5BTy1KMU94RDZyQW9aWjFnbTlBNGdPMVBoZmhNOXhuZWJkVzc1ZjNtQ2FlZGgxcVg0LVk1NUxUZkZSekIxWml5WnZlaEdHV2U2aW5YcGwtaEo4d1NNLUVLM0ROR1VmbG1NWlFnbzloanVlZTQzY2R3c0FZMFAzaHJScmM3cXJyMGJVdGxETml2a0NYdyIsInN1YnNjcmlwdGlvbklkIjoib2ttdXNpY2lhbi55ZWFybHkuZ3VpdGFyIn19', 'messageId': '611283052513650', 'message_id': '611283052513650', 'publishTime': '2019-07-10T06:10:35.838Z', 'publish_time': '2019-07-10T06:10:35.838Z'}, 'subscription': 'projects/evocative-radar-246211/subscriptions/sub_test_push'}

# 取消订阅
cancel_sub = {'message': {'data': 'eyJ2ZXJzaW9uIjoiMS4wIiwicGFja2FnZU5hbWUiOiJjb20ub2ttdXNpY2lhbi5hbmRyb2lkIiwiZXZlbnRUaW1lTWlsbGlzIjoiMTU2MjczOTA4MzMzOCIsInN1YnNjcmlwdGlvbk5vdGlmaWNhdGlvbiI6eyJ2ZXJzaW9uIjoiMS4wIiwibm90aWZpY2F0aW9uVHlwZSI6MywicHVyY2hhc2VUb2tlbiI6Im9lY21sbW5mbWVqZ2Jham5sZnBpZXBkZC5BTy1KMU94RDZyQW9aWjFnbTlBNGdPMVBoZmhNOXhuZWJkVzc1ZjNtQ2FlZGgxcVg0LVk1NUxUZkZSekIxWml5WnZlaEdHV2U2aW5YcGwtaEo4d1NNLUVLM0ROR1VmbG1NWlFnbzloanVlZTQzY2R3c0FZMFAzaHJScmM3cXJyMGJVdGxETml2a0NYdyIsInN1YnNjcmlwdGlvbklkIjoib2ttdXNpY2lhbi55ZWFybHkuZ3VpdGFyIn19', 'messageId': '611287925672884', 'message_id': '611287925672884', 'publishTime': '2019-07-10T06:11:23.692Z', 'publish_time': '2019-07-10T06:11:23.692Z'}, 'subscription': 'projects/evocative-radar-246211/subscriptions/sub_test_push'}


# 恢复订阅
restore_sub = {'message': {'data': 'eyJ2ZXJzaW9uIjoiMS4wIiwicGFja2FnZU5hbWUiOiJjb20ub2ttdXNpY2lhbi5hbmRyb2lkIiwiZXZlbnRUaW1lTWlsbGlzIjoiMTU2MjczOTY3ODU2MCIsInN1YnNjcmlwdGlvbk5vdGlmaWNhdGlvbiI6eyJ2ZXJzaW9uIjoiMS4wIiwibm90aWZpY2F0aW9uVHlwZSI6NywicHVyY2hhc2VUb2tlbiI6Im9lY21sbW5mbWVqZ2Jham5sZnBpZXBkZC5BTy1KMU94RDZyQW9aWjFnbTlBNGdPMVBoZmhNOXhuZWJkVzc1ZjNtQ2FlZGgxcVg0LVk1NUxUZkZSekIxWml5WnZlaEdHV2U2aW5YcGwtaEo4d1NNLUVLM0ROR1VmbG1NWlFnbzloanVlZTQzY2R3c0FZMFAzaHJScmM3cXJyMGJVdGxETml2a0NYdyIsInN1YnNjcmlwdGlvbklkIjoib2ttdXNpY2lhbi55ZWFybHkuZ3VpdGFyIn19', 'messageId': '611289414208777', 'message_id': '611289414208777', 'publishTime': '2019-07-10T06:21:19.52Z', 'publish_time': '2019-07-10T06:21:19.52Z'}, 'subscription': 'projects/evocative-radar-246211/subscriptions/sub_test_push'}

# 未知
null_sub = {'message': {'data': 'eyJ2ZXJzaW9uIjoiMS4wIiwicGFja2FnZU5hbWUiOiJjb20ub2ttdXNpY2lhbi5hbmRyb2lkIiwiZXZlbnRUaW1lTWlsbGlzIjoiMTU2MjczOTY1NTA0NiIsInN1YnNjcmlwdGlvbk5vdGlmaWNhdGlvbiI6eyJ2ZXJzaW9uIjoiMS4wIiwibm90aWZpY2F0aW9uVHlwZSI6MiwicHVyY2hhc2VUb2tlbiI6InBjcGxna2RrZ2tmZGpqZHBlaWRlYWpqbS5BTy1KMU95ZDE3VVBJd2pQQWFpb1BCRHlYQTZfZVlYLVZ2TXNUSlNxM2RvdlZMb2JzM19NUVlMYW9XbzRmLWxkSUVVZ2tKRnpzQlhHTVZiQm1vSDVCdllNdndjNmFPLWxoVExfejJzckppWVRuX1prQnpEclM5WEFyQXBHTFhiemJYeUY4T2dKS1hJNXNnVlB5Ukw0bmVORWItVk8zRXZBWUEiLCJzdWJzY3JpcHRpb25JZCI6Im9rbXVzaWNpYW4ubW9udGhseS5ndWl0YXIifX0=', 'messageId': '676529954566470', 'message_id': '676529954566470', 'publishTime': '2019-07-10T06:20:55.622Z', 'publish_time': '2019-07-10T06:20:55.622Z'}, 'subscription': 'projects/evocative-radar-246211/subscriptions/sub_test_push'}


ret = base64.b64decode(ret["message"]["data"])
cancel_sub = base64.b64decode(cancel_sub["message"]["data"])
restore_sub = base64.b64decode(restore_sub["message"]["data"])
null_sub = json.loads(base64.b64decode(null_sub["message"]["data"]))
print(ret, "\n")
print(cancel_sub, "\n")
print(restore_sub, "\n")
print(null_sub, "\n", type(null_sub))
print(null_sub["subscriptionNotification"]["subscriptionId"], "\n", type(null_sub))
print(null_sub["subscriptionNotification"]["purchaseToken"], "\n", type(null_sub))
