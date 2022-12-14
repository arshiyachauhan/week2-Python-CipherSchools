#string formatting
a=5
print("value of a is %d" % (a))
print("value of a is {}".format(a))
a,b,c=1,2,3
print("a= {2}, b= {1}, c= {0}".format(c,b,a))
name=["jatin","arshiya","vanshika"]
name="Jatin"
company="Dell"
print('Hello {name} welcome to my company {company}'.format(name =name, company=company))
print(f'name={name}')
print(len(r"a\nb")) #r modifier makes it a raw string

#other methods
print('    jatin    '.strip())
print("1,2,3,4,5".split(','))
print('jatin'.replace('a','u'))
print('arshiya'.count('a'))


