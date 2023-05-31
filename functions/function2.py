users = ["user1", "user2", "user3"]

def add(param):
    users.append(param)
    return users

users = add("user4")
print(users)


def addList(students,param):
    students.append(param)
    return students

students = addList(["raj","parth"],"user5")
print(students)

