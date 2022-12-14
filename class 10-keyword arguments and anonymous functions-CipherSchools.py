def func(a,b,c):
    print(a)
    print(b)
    print(c)
func(c=1,a=2,b=3)
def hello():
    print('Hello World !')
print(type(hello))
a=1
a= hello
a()
hello=2
print(hello)
def hello():
    return 1
print(hello)
print(hello())
#Arguments in python
#-Required arguments
def func(a,b):
    print(a,b)
func(1,2)
#-Default arguments
def func(a=1,b=2):
    print(a,b)
func()
func(1)
func(3,4)
#-Optional positional arguments
def func(*a):
    print(a)
func(1,2,3,4)
def func(a,b,*c):
    print(a)
    print(b)
    print(c)
func(1,2,3,4,"jatin",1.5)
#-Required keyworded only arguments-aadf
def func(a,b,*c,d,e="jatin"):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
func(1,2,3,d="something",e="aadf")
#-Default keyworded only arguments-jatin
#-Optional keyworded only arguments
def func(**k):
    print(k)
func(name='jatin')
print(sorted([1,5,3,4,2]))





