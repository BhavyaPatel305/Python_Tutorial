x =set(["naman","parth","kay","madam","malayalam","amit"])

#list1 =[i for i in x if i == i[::-1]]
#print(list1)
set1 ={i for i in x if i == i[::-1]}
print(set1)
print(type(set1))