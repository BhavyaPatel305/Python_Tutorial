# dict ={}
# set ={}

data = set({12,45,67,89,0,12})
print(data)
print(type(data))

data.add(133)
data.update({100,99})

data.update([12])


data.remove(12)
data.discard(100)

x = data.pop()
print(x)

un = data.union({11,22,456,99})
print("un...",un)


d = data.difference({1,2,89,12,45})
print("d...",d)
#data.difference_update({1,2,89,12,45})
i = data.intersection({1,2,89,12,45})
#data.intersection_update({1,2,89,12,45})
print("i...",i)

si = data.symmetric_difference({1,2,89,12,45})
print("si...",si)


print("subset",data.issubset({67}))
print("superset",data.issuperset({67}))



print("data",data)


# while data:
#     x = data.pop()
#     print(x)
    











# for i in data:
#     print(i)