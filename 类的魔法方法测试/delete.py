class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b


ac = A("A", "b")
# del ac.a
# print(ac.c)
# ac.__delattr__("c")
del ac.a, ac.b
print(ac.__dict__)
