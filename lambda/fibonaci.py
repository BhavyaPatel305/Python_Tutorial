from functools import reduce


#      lambda 10 : reduce(lambda x,_: x+[x[-1]+x[-2]],range(10-2),[0,1])
#      lambda 10 : reduce(lambda x,_: x+[x[-1]+x[-2]],range(8),[0,1])
           #                     x+[x[-1]+x[-2]]  x[-1] x[-2]
           #                     0+[0[-1]+0[-2]]    0     1
           #                     0+[1[-1]+1[-2]]    1     0 
#     
#     
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2),[0,1])
#fibonacci = lambda n: [0, 1] + [fibonacci(i - 1) + fibonacci(i - 2) for i in range(2, n)]

print(fib(10))

