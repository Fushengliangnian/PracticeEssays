import time
import functools

import tornado.ioloop
import tornado.web
import tornado.options
from tornado import gen
from tornado.httpclient import AsyncHTTPClient

tornado.options.parse_command_line()


def dec_demo(fn):
    @functools.wraps(fn)
    def inner(self, *args, **kwargs):
        print("执行之前")
        return fn(self, *args, **kwargs)
    return inner


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello, world")


class NoAsyncHandler(tornado.web.RequestHandler):
    @gen.coroutine
    @dec_demo
    def get(self):
        # s = yield gen.sleep(0.1)
        ret = yield self.doing()
        print(ret)
        self.write(ret)

    @gen.coroutine
    def doing(self, *args, **kwargs):
        print("？？？")
        time.sleep(5)
        raise gen.Return("5秒之后")


class AsyncHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch("http://www.baidu.com")
        print(1)
        time.sleep(5)
        print(2)
        self.write(response.body)


application = tornado.web.Application({
    (r"/index", MainHandler),
    (r"/async", AsyncHandler),
    (r"/no", NoAsyncHandler)
})

if __name__ == '__main__':
    application.listen(8989)
    tornado.ioloop.IOLoop.instance().start()
