class A():

    def __new__(cls):
        print("A.__new__ is called")
        print(type(cls), "\t", type(A))
        print(super())
        return super().__new__(A)

    def __init__(self):
        print("A.__init__ is called")


a=A()
