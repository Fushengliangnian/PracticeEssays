dic = {"a": 1}

while 1:
    try:
        a = dic["b"]
        print(a)
    except Exception as e:
        print(e)
        break

    finally:
        print("最后")
    print("。。。")

print("循环之外")
