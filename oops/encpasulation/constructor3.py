class Employee:
    
    name = None
    age = None
    salary = None
    
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        
        print("constructor is executed")
    
    def getEmps(self):
        print("name is: ",self.name)
        print("age is: ",self.age)
        print("salary is: ",self.salary)    
        


e1 = Employee("raj",20,10000)   
e2 = Employee("amit",30,20000) 

e1.getEmps()    
e2.getEmps()
        
    
    

        