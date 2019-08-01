import tornado.web
import tornado.ioloop
from tornado.gen import coroutine, Return
from motor import motor_tornado
from bson import ObjectId
import bson

client = motor_tornado.MotorClient('192.168.1.120', 30001)
db = client.piano


class LoginHandler(tornado.web.RequestHandler):
    @coroutine
    def get(self):
        document = {"key": "insert", "value": "insert_one"}
        ret = yield self.doing(document)
        print(ret)
        # print((yield ret.fetch_next))
        self.write("111")

    @coroutine
    def doing(self, document):
        ret = db.v1_category.aggregate([{'$match': {'instrument': {'$in': [4]}, 'state': 1}},
                                              {"$group": {'_id': '$category_type'}}])
        doc = []
        while (yield ret.fetch_next):
            doc.append(ret.next_object())
        raise Return(doc)

    @coroutine
    def count(self):
        print(db.demo1.count_documents({}))
        raise Return(db.demo1.count_documents({}))


application = tornado.web.Application([
    (r"/", LoginHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
