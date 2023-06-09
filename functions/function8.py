def add(a):
    print("Addition",a)
    def sqr(x):
        print("Square",x*x)
    sqr(a)

add(12) 


def test():
    return "ok"
    return "not ok" # this will not execute and not compilation error also

print(test())

def root(x):
    yield x+"ok" #flag True
    yield x+"not ok"
    yield x+"its ok"
    
    
for i in root("#"):
    print(i)
    print(type(i))




       