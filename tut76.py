#generator
def new(dict):
    for x,y in dict.items():
        yield x,y
a={1:"hii",2:"welcome"}
b=new(a)
print(b)
next(b)

#def myfunc(i)