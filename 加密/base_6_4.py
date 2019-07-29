import base64

ret = base64.b64encode(b"9999999")
print(ret, type(ret))
deret = base64.b64decode(ret)
print(deret)
