data = ("ram","krishna","shyam","hari","sita","gita")
print(data[0])

#data[0]="rama" #error

cnt = data.count("ram")
print(cnt)

ind =data.index("shyam")
print(ind)


for i in data:
    print(i)
    

data1 = ("ram","krishna","shyam","hari","sita","gita")
data2 = ("a","b","c","d","e","f")

data3 =()
print(data3)
print(type(data3))
data3 =("ok") #reinitialize not reasignmnet
print(data3)