#args

# def demo(a):
#     print(a)
    
# demo(100,200)    
    
def test(x,y,*args,**kwargs):
    print(type(args))
    print(x)
    print(args)
    print(kwargs)

test(100,200,300,name="raj")    