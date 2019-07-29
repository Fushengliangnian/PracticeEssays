import re

from services.response import Response


def index():
    body = '<!DOCTYPE html>\n<html>\n<head>\n<title>HTTP响应示例<title>\n</head>\n<body>\nHello HTTP!</body>\n</html>\n'
    return Response(body=body).to_show()


class Router(object):
    urlpatterns = [
        ("/", index),
    ]
    _obj = None

    def __init__(self, urlpatterns=[]):
        self.urlpatterns += urlpatterns

    def pipe(self, url):
        for pattern in self.urlpatterns:
            ret = re.search(pattern[0], url)
            if ret:
                return pattern[1]()
            return "err"

    def __new__(cls, *args, **kwargs):
        if not cls._obj:
            cls._obj = super().__new__(cls, *args, **kwargs)
            return cls._obj
        return cls._obj
