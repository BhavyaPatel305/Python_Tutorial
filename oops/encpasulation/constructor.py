#constructor is a function which has same name as class name: java,cpp
#constructor is used to initialize the instance variable
#constructor is executed automatically when we create object

class Employee:
    name = None #copy ?
    #no prameter constructor,default constructor
    # def __init__(self):
    #     self.name = "raj"    
    #     print("constructor is executed")

    def __init__(self,name):
        self.name = name
        


# emp1 = Employee() #constructor is executed        
# emp2 = Employee() #constructor is executed

emp1 = Employee("amit")
emp2 = Employee("rajesh")

#emp1.name = "raj"
print(emp1.name) #raj
#emp2.name = "rajesh"
print(emp2.name) #rajesh

