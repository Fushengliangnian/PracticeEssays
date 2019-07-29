from multiprocessing import Process

from redis import Redis


def target(i):
    r = Redis()
    ret = r.lpop("list_data")
    r.rpush("list_data", ret)
    print(ret, i)
    print(r.lrange("list_data", 0, -1), i)


if __name__ == '__main__':
    for i in range(2):
        Process(target=target, args=(i, )).start()
