import socketserver

from services.request import Request
from services.router import Router


class WSGIHandler(socketserver.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def handle(self):
        print("接收到请求：")
        environ = self.recv()
        request = Request(environ)
        url = request.path
        router = Router()
        response = router.pipe(url)
        print(response)
        self.send(response)
        print("返回响应")

    def recv(self):
        return self.request.recv(9999)

    def send(self, response, **kwargs):
        self.request.send(response)
