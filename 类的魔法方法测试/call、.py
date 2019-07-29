class A:

    def __call__(self, *args, **kwargs):
        def aaa():
            return 3
        return aaa


# a = A()
# print(type(a()()))


def func(a: int, b: str):
    print(type(a), type(b))


# func("1", 2)

while 1:
    a = bool(input())
    if a is True:
        print("...")
    print("not a\n")
