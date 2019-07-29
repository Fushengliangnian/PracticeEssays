import tornado.web
import tornado.ioloop
from tornado import gen

import tornado_mysql
from tornado_mysql import pools

POOL = pools.Pool(
    dict(host='127.0.0.1', port=3306, user='root', passwd='123', db='cmdb'),
    max_idle_connections=1,
    max_recycle_sec=3)


@gen.coroutine
def get_user_by_conn_pool(user):
    cur = yield POOL.execute("SELECT SLEEP(%s)", (user,))
    row = cur.fetchone()
    raise gen.Return(row)


@gen.coroutine
def get_user(user):
    conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='cmdb',
                                       charset='utf8')
    cur = conn.cursor()
    # yield cur.execute("SELECT name,email FROM web_models_userprofile where name=%s", (user,))
    yield cur.execute("select sleep(10)")
    row = cur.fetchone()
    cur.close()
    conn.close()
    raise gen.Return(row)


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')

    @gen.coroutine
    def post(self, *args, **kwargs):
        user = self.get_argument('user')
        data = yield gen.Task(get_user, user)
        if data:
            print(data)
            self.redirect('http://www.baidu.com')
        else:
            self.render('login.html')


application = tornado.web.Application([
    (r"/login", LoginHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
