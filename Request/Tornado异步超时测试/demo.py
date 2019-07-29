import time
import functools

import tornado.ioloop
import tornado.web
import tornado.options
from tornado import gen

tornado.options.parse_command_line()


class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        time.sleep(6)
        self.write("7777")


application = tornado.web.Application({
    (r"/", MainHandler),
})

if __name__ == '__main__':
    application.listen(8980)
    tornado.ioloop.IOLoop.instance().start()
