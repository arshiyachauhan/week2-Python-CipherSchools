#lists are ordered and can be indexed using positions
#dicts are unordered and can be indexed using keys
#sets are unordered and cannot be indexed
a={1,2,3,4}
print(type(a))
print(list(a))
a.add(7)
a.add(6)
a.remove(3)
for i in a:
    print(i)
a={1,2,3,4}
b={3,4,5,6}
print(a-b)
print(a.union(b))
print(a.intersection(b))
a.remove(3)
print(a)
a=[['']*3]*3
a[1][1]='x'
print(a)

#is operator
a=255
b=255
print(a is b)
a=258
b=258
print(a == b)
print( a is b)
print(id(256))
 
a=(3,2,1)
hash(a)