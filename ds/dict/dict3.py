list1 = [13,23,35,4,5,6,7]
list2 =[11,22,33,44,55,66,77]
dict={}

dict2 = list(zip(list1,list2))
print(dict2)

for i in range(0,len(list1)):
    dict[list1[i]]=list2[i]
   
   
print(dict)    