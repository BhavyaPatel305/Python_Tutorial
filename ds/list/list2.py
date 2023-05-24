users = ["raj","ram","parth"]
#list is mutable : after declaration we can add or remove elements
users.append("ravi")
users.insert(1,"meet")

users.extend(["manan","mehul","mohit"])

print(users)

ind = users.index("ram")
print("index is ",ind)

#pop is overloded function
# rmvelm = users.pop()
# removedelm = users.pop(3)
# print("removed element is ",removedelm)

# cnt =users.count("ravii")
# print("count is ",cnt)

# users.remove("ravi")

#users.sort()
#users.sort(reverse=True)

#users.clear()
#print(users)

#susers.reverse()
# usercopy = users.copy()
# print(usercopy)

# usercopy.append("royal")

for i in users:
    print(i)
    