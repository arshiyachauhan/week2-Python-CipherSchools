print(lambda a,b:a+b)
show=print
show("something")
def func():
    return 1+4
a=func
print(a())
#[]are used to define an arey
names=["jatin","arshiya","vanshika"]
for name in names:
    print(name)
for name in enumerate (names):
    print(name)

#swaping values
a=5
b=6
a,b = b,a
print(a,b)
a=1,2
print(type(a))
names=["jatin","arshiya","vanshika"]
for i in enumerate (names):
    print(i,"-",name)
names=["jatin","arshiya","vanshika"]
scores=[79,89,94]
states=["delhi",'himachal','punjab']
for name,score,state in zip(names,scores,states):
    print(name,"-",score,state)