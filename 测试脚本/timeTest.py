import time
from threading import Thread
from multiprocessing import Pool

import requests


def take(i):
    # url = "http://127.0.0.1:33333/v1/score/home/"
    url = "http://123.206.19.158:33333/v1/score/home/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36",
        "platform": "1",
        "Version": "1.0",
        "instrument-type": "4"
    }
    old = time.time()
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        new = time.time()
        print(f"第{i}号进程")
        print("ok, time: ", new - old)


if __name__ == '__main__':
    print("##### 开始 ######")
    old = time.time()
    pool = Pool(10)
    # for i in range(1000):
    #     tk = Thread(target=take, args=(i,)).start()
    pool.map(take, list(range(1000)))
    print("##### 结束 #####")
    new = time.time()
    print("time: ", new - old)