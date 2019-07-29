import requests
from multiprocessing import Pool
import time


def func(i):
    url = "http://127.0.0.1:8989/"
    # data = {"phone": 17611097053}
    old = time.time()
    response = requests.get(url)
    ret = response.content
    print(f"第{i}个")
    print(response.status_code)
    print(ret)
    print(time.time() - old)


if __name__ == '__main__':
    print("开始")
    pool = Pool(10)
    pool.map(func, range(1000))
    print("结束🌈")
