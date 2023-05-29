sales ={"team1":[12,22,33,44,55,66,78],"team2":[45,67,8,9,76,45,67]}
print(sales)

listsum=[]
sum=0

for i,j in sales.items():
    print(i)
    for k in j:
        print(k)
        sum = sum+k
    print("sum=",sum)
    listsum.append(sum)
    sum=0
    print("-----------")   
    

print(listsum)     

maxelm = max(listsum)
print("max -->",maxelm)
ind = listsum.index(maxelm)

print("max sales team is",ind+1)