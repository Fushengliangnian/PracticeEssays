import time

print(time.localtime())

format_time = time.strftime("%Y-%m-%d")
struct_time = time.strptime(format_time, "%Y-%m-%d")
timestamp = time.mktime(struct_time)
print(timestamp)
