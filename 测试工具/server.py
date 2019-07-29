import random

import tornado.ioloop
import tornado.web
from tornado import gen
from tornado.web import RequestHandler


class AsyncSleepHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        yield gen.sleep(random.random() / 10.0)
        self.write('sleep')


class Async2SleepHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        yield gen.sleep(random.random() / 10.0 * 2)
        self.write('sleep')


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/sleep", AsyncSleepHandler),
        (r"/sleep2", Async2SleepHandler),
    ], debug=1)
    application.listen(8888)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.current().stop()
