import time

# ret = time.struct_time("%Y-%m-%d")
ret = time.localtime()
# print(ret[0], type(ret[1]), ret[2], ret[3])
# print(ret)

a = b"1"
b = b"2"
print(max(a, b))
