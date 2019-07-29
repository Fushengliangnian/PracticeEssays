# import sentry_sdk
#
# sentry_sdk.init("https://c3431256c31d46d6b37acd07510a3461@sentry.io/1399157")
# l = 99 // 100 % 2
# print(l)
# lis = []
# print(lis[0])
# print(lis[:1])


def fu():
    def cc():
        print(666)
        return 10

    return cc()


for i in range(3):
    print(fu())
