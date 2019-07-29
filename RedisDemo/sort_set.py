import redis


r = redis.Redis()
res = r.zrevrange('hot_rank', 0, -1, withscores=True)
print(res)
for i, j in res:
    print(i, j)
