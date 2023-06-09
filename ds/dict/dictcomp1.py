data = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}
dict ={}
for i in data:
    if len(data.get(i))>3:
        dict[i] = data.get(i)
print(dict)        


for i,j in data.items():
    if len(j)>3:
        dict[i] = j

print(dict)        
    
    
dict2 = {i:j for i,j in data.items() if len(j)>3}
dict3 = {i:data.get(i) for i in data if len(data.get(i))>3}
print(dict2)    
print(dict3)