import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 9999))
sk.listen(10)
while 1:
    conn, addr = sk.accept()
    ret = conn.recv(9999)
    print(ret)
    conn.send(ret)
    conn.close()
