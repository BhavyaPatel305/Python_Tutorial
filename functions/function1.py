#without return type and without argument
def sum():
    print("sum of 2 and 3 is:",2+3)

def add(a,b):
    c = a + b
    return c
    #return a + b

#withput parm / arg and with return type
def pow():
    return 2**3

sum()
x = add(100,200)  
print(x)  
print(add(10,20))

y = pow()
print(y)
print(pow())
