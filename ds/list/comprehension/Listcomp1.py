users = ['Marry', 'Tom', 'Jack', 'Rose', 'Alice','Mira']
# filUsers =[]

# for i in users:
#     if len(i)>3:
#         filUsers.append(i)
        
# print(filUsers)        

filUsers = [i for i in users if len(i)>3 and i.startswith('M')]
print(filUsers)


