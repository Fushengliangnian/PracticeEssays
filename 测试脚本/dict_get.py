
dic = {"a": "b"}


class B:
    def __init__(self):
        print("b+")


class A:
    def __init__(self, app):
        self.app = app
        self.app.config = app
        self.app.config.a = "b"

    def get_a(self):
        return getattr(self.app.config, "a", None)


a = A(B())
print(a.get_a())

ret = getattr(dic, "a", None)
print(ret)

