#elif in lambda
res = lambda x,y : "x is greater" if x>y else "y is greater"
print(res(10,20))

res1 = lambda x,y : "x is greater " if x<y else("x is equal" if x==y else "y is greater")

print(res1(10,20))
print(res1(20,10))
print(res1(10,10))

