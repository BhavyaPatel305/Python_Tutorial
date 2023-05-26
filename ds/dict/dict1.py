ranks ={1:"ajay",3:"vijay",2:"sanjay",4:"jay",3:"VIJAY"}
print(ranks)
k = ranks.keys()
print(k)
v = ranks.values()
print(v)
items = ranks.items()
print(items)

ranks[78]="sachin"
ranks[3]="vikas"

ranks.update({7:"Dhoni"})
ranks.update({2:"kohli"})
ranks.update({3:"Rohit",44:"Rahul"})

#remove

removedelm = ranks.pop(2)
print("removing....",removedelm)

removeitem =ranks.popitem()
print("removing....",removeitem)


vl = ranks.get(3) #it return None if key is not present
print("get value from key",vl)

#newdic  = ranks.fromkeys([1,2,3,4,5,6],"ajay")
#print("new dict",newdic)
data = {}
data= data.fromkeys([1,2,3,4,5,6],"ajay")
print("new dict",data)



for k,v in ranks.items():
    print(k,v)


