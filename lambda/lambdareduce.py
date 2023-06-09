#filter predicate true or false ["a","b","ccc","xpy"]
# false, false, true, true
#map return value
#[1,2,3,4,5,6] [1,4,9,16,25,36]
#reduce return single value 
# [1,2,3,4,5,6] 21
from functools import reduce
li = [1,2,3,4,5,6]
sum = reduce((lambda x,y: x+y),li)
print(sum)

li = [11,45,67,89,4,3,78]
max = reduce((lambda x,y: x if x>y else y),li)
print(max)

#using reduce find number of occuring even numbers in the list

data = [100,200,45,67,89,0]

ans = reduce((lambda x,y: x+1 if y%2==0 else x),data,0)
print(ans)

#string concatenation using reduce ["a","b","c","d"] "abcd"