from datetime import datetime


class Response(object):
    base = "HTTP/1.1 %d OK\r\nDate: %s GMT\r\nLast-Modified: Tue, 22 Jan 2019 10:32:30 GMT\r\nServer: nginx/1.4.6 (Ubuntu)\r\nContent-Encoding: gzip\r\nContent-Type: %s\r\n"

    def __init__(self, body, code=200, content_type="text/html"):
        self.header = self.base % (code, datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S'), content_type)
        self.body = body

    def to_show(self):
        return (self.header + self.body).encode("utf8")

    def render(self):
        pass

    def redirect(self):
        pass

    def json(self):
        pass

    def send_file(self):
        pass
