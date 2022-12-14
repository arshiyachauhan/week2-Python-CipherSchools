def show_loading():
    for _ in range(3):
        print(_)
        print('loading...')
a=5
b=7
print(a+b)
show_loading()
print(a-b)
show_loading()
def sheldon_knock(name,times=3):
    for _ in range(times):
        print("knock knock knock", name)
sheldon_knock("leonard",20)
def add(a,b):
    return a + b
a= add(2,4)
print(a)
