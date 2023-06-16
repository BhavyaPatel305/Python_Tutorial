class Emp:
    
    name = None
    def __init__(self,name):
        self.name = name
        
    def printName(self):
        print("name is: ",self.name)
        

objlist =[]
for i in range(3):
    #user...
    name = input("enter name: ")
    emp = Emp(name)            
    objlist.append(emp)
    

for i in objlist:
    i.printName()    