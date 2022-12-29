student1={"name":"Jatin","marks":100}
student2={"name":"Samarth", "marks":50}

#python object can have m ultiple attribbutes
#callable,iterable,contextable
class person:
    pass
p=person()
print(p)
a=1
def square(a):
    print(a**2)
print(hex(id(p)))
class Person:
    name:"Jatin"
    def say_hi(this):
        print("Hello everyone ! I am (this.name)")
p=Person()
p.say_hi() #method call
Person.say_hi(p) # function call