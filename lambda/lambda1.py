def sum(a):
    print("sum() is called")
    
    
sum(10)

#conver to lambda

x = lambda a:print("sum() is called...",a)
x(10)

def add(a,b):
    return a+b

ans = add(10,20)
print(ans)
print(add(10,21))

s = lambda a,b:a+b
ans1 = s(11,21)
print(ans1)

#12 22

def comp(a,b):
    if(a>b):
        return a
    return b


c = comp(10,20)
print(c)


comp1 = lambda a,b :a if a>b else b
print(comp1(10,200))


def cube(a):
    return a*a*a

lambda_cube = lambda a:a*a*a
print(lambda_cube(10))





    


    