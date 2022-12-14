#in lists actual value can be changed
#tuple starts with -() and values cannot be changed
a=(1,2,3,4)
print(type(a))
def func(*args):
    print(type(args))
func(1,2,3,4)
a=4
b=6
c= a,b
print(type(c))
def sum_diff(a,b):
    s=a+b
    d=a-b
    return s,d
a=(1,2,3)
print(list(a))
#Dictionary -{}
a={"name": "jatin",
   "company": "shell",
   "college": " LPU"}
print(a['company'])
key='marks'
if key is a :
    print(a[key])
else:
    print("key doesnot exist")
key='marks'
print(a.get(key))
key= "name"
print(a.get(key))
print(a.keys())
print(a.values())
for x in  a.items():
    print(x)
for key,value in a.items():
    print(key, '-->', value)
a={'name':'jatin','college':'LPU','company':'SHELL'}
for x in a:
    print (x)
print(list(a))