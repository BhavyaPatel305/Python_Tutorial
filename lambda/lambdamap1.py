li = [1,2,4,6,7,90,45]
sqrlist = list(map(lambda x: x**2,li))
print(sqrlist)

users =["ram","jay","parth","harsh","het"]
usersupr = list(map(lambda x: x.upper(),users))
print(usersupr)

#map with if else

sqrlist2 = list(map(lambda x: x**2 if x%2==0 else x**3,li))
print(sqrlist2)

# if name contains space make it title case
["ram patel"]
# Ram Patel


# for i in li:
#     x = i**2
#     sqrlist.append(x)

# print(sqrlist)    