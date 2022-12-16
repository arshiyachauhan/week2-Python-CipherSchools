import platform


a=[]
for i in range(5):
    a.append(i)
print(a)

#comprehension method
[i for i in range(5)]

list(map(lambda x: x**2,range(5)))
a=[]
for i in range(5):
    a.append(i**2)
print(a)
#list comprehension
a=[]
for i in range(5):
    temp=[]
    for j in range(5):
        temp.append(j)
    a.append(temp)
print(a)
n=5
l=[[max(i+1,j+1,n-i,n-j )for j in range(n)]for i in range(n)]
print(l)
p=[i for i in range(5)]
print(p)
a=[]
for i in range(2):
    for j in range(2):
        a.append(j)
print(a)
#dictionary comprehension
print({2:4,3:9,4:16})
a={i:i**2 for i in range(5)}
print(a)
print(type(a))
#set comprehension
a={i for i in range(5)}
print(a)
print(type(a))
a=(i for i in range(5))
print(type(a))
#generator is lazy loading,it will iterate but not give the value of a.