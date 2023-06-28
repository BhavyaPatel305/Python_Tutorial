file = open("C:\\Users\\Samir\\Desktop\\dictonry","r")

# for i in file:
#     print(i,end="")
    

# file.readlines()
# file.readline()    

x = file.readlines()
print(x)

while True:
    line = file.readline()
    if line == "":
        break
    print(line,end="")

