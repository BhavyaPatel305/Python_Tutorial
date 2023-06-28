file = open("demo.txt","r")
count=0 

# for i in file:
#     count+=1
#     print(i,end="")

#read data character by character

# for i in file.read():
#     print(i,end="")
#     count+=1

#read data by word by word

for i in file.read().split():
    print(i)
    count+=1

print("Total lines in file:",count)    
# s = file.read(10)
# print(s)