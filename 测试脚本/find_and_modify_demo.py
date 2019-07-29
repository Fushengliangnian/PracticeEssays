import pymongo
import random


client = pymongo.MongoClient(host="127.0.0.1", port=27017)
db = client.testDemo
table = db.demo1

ret = table.find_and_modify({}, {"key": random.random()})
print(ret)
