import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 9999))
sk.send(b"hello, word")
ret = sk.recv(1024)
print(ret)
sk.close()
