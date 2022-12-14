#[]are used to make lists
a=[1,2,3,4]
print (a)
a=[1,2,3]
a[0]=100
print(a)
print(len('arshiya'))
print("ars"+'hiya')
print([1,2,3]+[4,5,6])
print([1]*4)
a=[1,2,3]
for x in a:
    print(x)
print('a' in 'jatin')

#indexing and list slicing
a=[1,2,3,4]
print(a[-1])
a=[1,2,3]
a.insert(1,100)
print(a)
a.append(4)
print(a)
a.pop()
print(a)
a=['jatin','samarth','jatin','mahesh']
a.remove('jatin')
print(a)
a.remove('jatin')
print(a)

#listing and slicing
a=[4,3,2,1,5]
a.sort()
print(a)
b=[1,4,5,3,2]
print(sorted(a))
print(b)
print(reversed(b))
print(b)
#map,strip and split function
a=[1,2,3,4]
for x in map(lambda x: x**2,a):
    print(x)
x=[1,2,3,4]
a= map(int,input(x).split())
print(x[0])
print(','.join(['jatin','sam','solly']))



