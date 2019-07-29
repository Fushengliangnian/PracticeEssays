import pymongo

mongo = pymongo.MongoClient(host="123.206.19.158", port=30001)
db = mongo.piano
table = db.v1_score_manage
if __name__ == '__main__':
    items = [{'_id': 1}, {'diff': -1.0}, {'instrument': 1.0}, {'category': 1.0},
             {'desc': 'text', 'name': 'text', 'author': 'text'}, {'hot': -1.0}, {'instrument': 1.0, 'state': 1.0},
             {'state': 1.0}]

    for item in items:
        ret = table.create_index(list(item.items()))
