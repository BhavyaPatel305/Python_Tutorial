def divide(func): #3
    
    #division
    def inner(a,b): #6
        print("I am going to divide",a,"and",b) 
        if b == 0: #8
            print("Whoops! cannot divide")
            return
    
        return func(a,b) #division(100,2) #8
    
    return inner #4


@divide #2, #5
def division(a,b): 
    print("....")
    return a/b #9 #100/2

x  = division(100,0)     #1
print(x)