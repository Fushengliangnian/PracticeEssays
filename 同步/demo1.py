from multiprocessing import Process

# 同步
def func(n):
    import time
    time.sleep(0.2)
    print(n)

# 异步
def async_func(n):
    import time
    time.sleep(0.2)
    print(n)


if __name__ == '__main__':
    for i in range(10):
        p = Process(target=async_func, args=(i,)).start()
