import pymongo
import random

db = pymongo.MongoClient(host="127.0.0.1", port=27017)
coll = db.testDemo.sort_test_demo

n = 50
for i in range(50):
    if n % 2 == 0:
        coll.insert({"key1": n, "key2": random.randint(0, 100)})
        n -= 1
        continue
    n -= 1
    coll.insert({"key1": n, "key2": random.randint(0, 100)})
