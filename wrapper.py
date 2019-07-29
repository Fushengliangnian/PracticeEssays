def a(fun):
    def wrapper(*args, **kwargs):
        q = 1
        ret = fun(q, *args, **kwargs)
        # return ret

    return wrapper


def b(fun):
    def wrapper(*args, **kwargs):
        w = 2
        ret = fun(w, *args, **kwargs)
        # return ret

    return wrapper


def c(fun):
    def wrapper(q, w, *args, **kwargs):
        e = 3
        print(w)
        ret = fun(e, w, q, *args, **kwargs)
        # return ret

    return wrapper


@a
@b
@c
def fun(q, w, e, *args, **kwargs):
    print(q, w, e)


fun()

# with open("file.text", "r", encoding="utf8") as f:
#     for i in f:
#         print(i)


s = "xixxxxx"
i = "i"

if i in s:
    s.replace(i, "x")

l1 = [1, 2, 3]
l2 = [2, 3, 4]

# 交集
l3 = [i for i in l1 if i in l2]
# 差集
l4 = [i for i in l1 if i not in l2]

# 转浮点型
a = "1234"
print(float(a))  # 值为 1234.0

# 列表
s = "abcd"
ls = s.split()
# or
ls2 = list(s)
# or
ls3 = [i for i in s]
print(ls, ls2, ls3)

# 数组
l = [1, 2, 3, 4, 5]
t = tuple(l)
print(t)

from multiprocessing.pool import Pool
import os


def ix_to_vx(n):
    os.system(f"encoder -i i{n}.yuv -o o{n}.yuv")
    if not os.path.exists(f"i{n}.yuv"):
        print("i{n}.yuv ok")
        return
    print("i{n}.yuv not ok")
    return


if __name__ == '__main__':
    # p = Pool(8)
    # p.map(ix_to_vx, range(1, 9))
    import json

    # print(json.dumps({
    #     'Store': 'GooglePlay',
    #     'TransactionID': 'GPA.3341-4166-2047-19888',
    #     'Payload': '{"json":"{"orderId":"GPA.3341-4166-2047-19888","packageName":"com.okmusician.trivialdrivesample","productId":"com.musician.test.infinite_gas_yearly","purchaseTime":1559289764781,"purchaseState":0,"developerPayload":"{"developerPayload":"","is_free_trial":false,"has_introductory_price_trial":false,"is_updated":false}","purchaseToken":"neiaeebdhjjadoeknihieikh.AO-J1OyJ71hrGAhXoJf10_aHVvzFvY_Bkv95Shrn0dVzdzfEiWhk5Li9Mb42p-Y1ybzjt3hjZquiAPfoJGeJLxNTSB-nwplR11-ZMjGm3k0r-vmlsm8RaTmTk24Lr4QkgldvXPaUlViTdxHtgLlpw6oHAVSDKcKUO6uczOkrZSgzWMhU8oWXbBk","autoRenewing":true}","signature":"GB3wth0tcxrVSESvo6lqW1d52Q7AnZVyDWgaJ1i6q1qz473nNkmKmLuya+aVRijT8eEwmEmm+VlgCtCmrqX0bDgj4PR7FfJp0tOyyHYddMwkh9G9vF9wVFHa33BS8rjdb3POObVFaiVTFcN2SPZPnJV1YeUOOWDb2Hpdr3a6js/ovIC5+uTBHi7kH7bhIO53hZ752x+XtZlNXyjmpxVGmJ5AF+gQJgwZuqcbQ1392Fkz2vggWRQ/VKW5585VWD+h2hct0sji4B/W79fH5v6BBGSEDWkrjc8wMpmL/f2ElyXPv/NDLpREfXJnqm0EFAsEScacNgXiRVG33sXPQ3wPhQ==","skuDetails":"{"skuDetailsToken":"AEuhp4JY0Maj-mogpTtz3RKxCG-sfVVLoG7E6HQbxZH-2b_zxZZhxblupOiExxYv2L5g","productId":"com.musician.test.infinite_gas_yearly","type":"subs","price":"US$2.99","price_amount_micros":2990000,"price_currency_code":"USD","subscriptionPeriod":"P1Y","freeTrialPeriod":"P3D","title":"infinite_gas_yearly (OKMusician)","description":"infinite_gas_yearly"}","isPurchaseHistorySupported":true}'
    # }))
    print(str(None))
