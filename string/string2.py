name = "java1_"
x = name.startswith("J")
print(x)
x = name.endswith("a")
print(x)

name = name.upper()
print(name)

x = name.isalpha()
print(x)
x = name.isalnum() #alpha numeric
print("alnum",x)
x = name.isdigit()
print(x)

name = "hello this is python"
#name = name.capitalize()
#name = name.title()
print(name)

cnt = name.count(" ")
print(cnt) #wo function use 

#name = name.replace("ll","#")
ind = name.index("l")
# print(ind)
print(name)

name ="python java node js"
x = name.istitle()
x  = name.islower()
x = name.isupper()
x = name.isascii()

f  =name.find("o",0,5)
print(f)
print(x)

list = name.split("p")
print(list)


#name = name.center(10,"*")
print(name)




name = "saamir"

name = name.replace("a","A",1)

print(name) 

