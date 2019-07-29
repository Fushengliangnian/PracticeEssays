import redis

r = redis.Redis(host="192.168.1.120", port=23781)
ret = r.keys()
print(ret)
for key in ret:
    value = r.get(key)
    print(key, ":", value)
