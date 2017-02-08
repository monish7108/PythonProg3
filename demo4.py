class A():
    numOfInstances=0

    def __init__(self):
        self.count()
    @classmethod
    def count(cls):
        cls.numOfInstances+=1

class B(A):
    numOfInstances = 0

class C(A):
    numOfInstances = 0

class D(A):
    pass

a=A()
b1,b2=B(),B()
c1,c2,c3,c4=C(),C(),C(),C()
print(A.numOfInstances)
print(B.numOfInstances)
print(C.numOfInstances)