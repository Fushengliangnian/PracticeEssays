import socketserver

from wsgi.wsgi import WSGIHandler
import settings

server = socketserver.TCPServer((settings.IP, settings.PORT), WSGIHandler)
server.serve_forever()
