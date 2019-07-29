import json
import time
import functools

import tornado.ioloop
import tornado.web
import tornado.options
from tornado import gen
from tornado.httpclient import AsyncHTTPClient, HTTPRequest

tornado.options.parse_command_line()

url = "http://127.0.0.1:8980/"


class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        old = time.time()
        response = yield AsyncHTTPClient().fetch(HTTPRequest(
            url='http://127.0.0.1:33333/v1/aimusic/score/?diff=%s&label=%s&page=%s&size=%s' % (
                "general", "b1909939-429b-42d5-a22e-bbf9247a5b5f", 0, 20)))
        print(response.code)
        data = json.loads(response.body)
        print(data, "\n\n")
        # TXconfig()
        self.write(str(response.code))


application = tornado.web.Application({
    (r"/", MainHandler),
    # (r"/async", AsyncHandler),
    # (r"/no", NoAsyncHandler)
})

if __name__ == '__main__':
    application.listen(8989)
    tornado.ioloop.IOLoop.instance().start()
