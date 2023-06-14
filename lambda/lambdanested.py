# def test():
#     def demo():
#         print("Hello World")
#     demo()

# test()    
        
ans = lambda a,b: lambda c:a+b+c
x = ans(100,20)
print(x)
print(x(30))

#----------------------
sq = lambda x: x**2
pr  = lambda fun,n : lambda x : fun(x)*n

ans = pr(sq,2)(10)
print(ans)

#Royal ENFIELD

sqr = lambda x: x**2 if x %2 == 0 else x**3
ans = lambda fun,n : lambda x : fun(x)**n
print(ans(sqr,2)(2))



fun1 = lambda x : x**2 if x%2 == 0 else x**3

fun2 = lambda fun : lambda x: fun(x)*2


ans = fun2(fun1)(3)
print(ans)

















