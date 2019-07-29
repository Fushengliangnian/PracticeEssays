import redis

client = redis.Redis()
# lis = ['U:167565880', 'U:208934934', 'U:123609895', 'U:180805384', 'U:116205417', 'U:118908532', 'U:268173260', 'U:191714863', 'U:235422640', 'U:255598840', 'U:248954420', 'U:110734357', 'U:261124310', 'U:113373944', 'U:235025561', 'U:174834810', 'U:239322044', 'U:242405886', 'U:259799135']
#
# for index, v in enumerate(lis):
#     print(index)
#     client.set(v, index)

client.sadd("device_id_set", "sss")
ret = client.smembers("device_id_set")
print(ret)
