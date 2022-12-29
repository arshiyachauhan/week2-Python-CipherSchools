a=1
print (a+1)
print(str(a))
#identification of dunders: __<name of dunder>__
class A:
    def __init__(self):
        print("initializer")
    def __del__(self):
        print("I am dying")
a=A()
print(a)
#raise Exeption() inside function would not create object a in python
#this behaviour happens when init is a constructor
a=1
print(a.__add__(5))
print("jatin".__mul__(2))
class A:
    a=1
    b=2
    def __add__(self,x):
        return self.a+self.b+x
a=A()
print(a+3)

