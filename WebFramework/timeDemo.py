import datetime

ret = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S')
print(ret)


import requests

ret = requests.get("http://127.0.0.1:9090")
print(ret.content)
