# -*- coding: utf-8 -*-
import bson

import pymongo
import time

old = time.time()

mongo = pymongo.MongoClient(port=30001)
db = mongo.piano
table = db.v1_score_manage
# table = db.v1_score
# table = db.v1_collection_manage
# table = db.v1_collect
# table = db.v1_category

# ret = table.find({
#     # "$text": {"$search": "peilun"},
#     # "$or": [{"_id": bson.ObjectId("5c35a0da191e7549cc81d742")}, {"_id": bson.ObjectId("5c35a0f7191e7549d52714f6")}],
#     # "_id": {"$in": [bson.ObjectId("5c35a0da191e7549cc81d742"), bson.ObjectId("5c35a0f7191e7549d52714f6")]}
#     # 'instrument': {'$in': [4]},
#     # 'state': -1,
#     # "create_at": {"$gt": 15466008, "$lt": 15466008450},
#     # {'instrument': {'$in': [4]}, 'state': {'$in': [1, 2]}, '$text': {'$search': '拜厄钢琴教学曲库'}}
#     # 'category': {'$in': ['new']},
#     # 'instrument': {'$in': [4]},
#     # 'state': {'$in': [1, 2]},
#
#     # 'category': {
#     #     '$in': ['popular']
#     # },
#     # 'score_ids.0': {
#     #     '$exists': 1
#     # },
#     # '$text': {
#     #     '$search': '钢琴'
#     # },
#     'instrument': {
#         '$in': [4]
#     },
#     'state': 2,
#     "bgt": {'$ne': {}},
#     'diff': {'$gte': 0}
#
# # '$or': [{
# #     'create_at': {
# #         '$gt': 1451577600.0,
# #         '$lt': 1547049600.0
# #     }
# # }, {
# #     'add_time': {
# #         '$gt': 1451577600.0,
# #         '$lt': 1547049600.0
# #     }
# # }]
# # })
# # # ret = table.find()
# # print(list(ret))
# # # print(type(table))
# # # from pymongo.collection import Collection
# # # ret = table.update_many({'batch_number': 999})
# # # print(ret)
# # for i in list(ret):
# #     print(i)
#
#     # import uuid
#     #
#     # print(uuid.uuid4(), type(str(uuid.uuid4())))
#
#     # ret_list = list(table.find({}))
#     # print(ret_list)
#     #
#     # for ret in ret_list:
#     #     print("#########")
#     #     print(ret)
#     #     ret["batch_number"] = "999"
#     #
#     #
#     # table.update()
#
# table.update()

# table.update_many(
#     {},
#     {"$set": {"state": 1}},
#     )

# ret = table.find({})
# data = []
# for item in list(ret):
#     cover = item.get("cover")
#     name = item.get("name")
#     data.append({cover: name})
#
# print(data)
#
# item = [u'new', u'classical', u'course', u'popular', u'new', u'classical', u'movie', u'cartoon', u'reminiscence',
#         u'vip', u'jazz', u'song', u'game', u'child', u'mood', u'famous', u'english', u'lightmusic', u'strawberry',
#         u'valentine', u'chinese', u'piano', u'theatre', u'other', u'test', u'popular', u'new', u'child', u'cartoon',
#         u'movie', u'course', u'other']
# print(len(item))
# pipeline = [{'$match': {"instrument": {'$in': [4]}, "state": 1}, "category": {'$in': ["recommend"]}},
#             {"$unwind": "$category"},
#             {'$sample': {'size': 15},
#              {'$group': {'_id': '$category', 'group_avg': {'$avg': "$hot"}, "group_count": {"$sum": 1}}}]

# pipeline = [{'$match': {'instrument': {'$in': [4]}, 'state': 1}},
#             {"$unwind": "$category_type"},
#             {"$group": {'_id': '$category_type'}}]
#
# ret = table.aggregate(pipeline)
# #
# # dic = {}
#
# # ret = table.find({"instrument": {'$in': [4]}, "state": 1, "category": {'$in': ["recommend"]}})
# print(time.time() - old)
# print(list(ret))
# for i in ret:
#     print(i)
old = time.time()
ret1 = table.find({"_id": bson.ObjectId('5c3897f5191e7581fdc2bebe')})
ret2 = table.find({"_id": bson.ObjectId('5c389899191e75825d93d1b6')})
ret3 = table.find({"_id": bson.ObjectId('5c389912191e7582695651df')})
print("find three time: ", time.time() - old)    # 0.00023603439331054688
print(ret1, ret2, ret3)

# old2 = time.time()
# ret = table.find({"_id": {"$in": ["5c3897f5191e7581fdc2bebe", "5c389899191e75825d93d1b6", "5c389912191e7582695651df"]}})
# print("find one time: ", time.time() - old2)  # 0.00017189979553222656
# print(ret)

# table.save()

