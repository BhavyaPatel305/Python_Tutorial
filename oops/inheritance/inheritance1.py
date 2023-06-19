#single inheritance a --> b
class Vehicle():
    #parent class
    makeyear =0  # class variable / instance variable
    vehtype =""
    
    def vehilceData(self):
        print("vehicle data")
        
    def __init__(self):
        print("vehicle constructor")
            
    
class Car(Vehicle):
    
    # def __init__(self):
    #     super().__init__() #calling parent class constructor
    #     print("car constructor")
    
    def getCarData(self):
        self.makeyear  = int(input("Enter make year: "))
        self.vehtype = input("Enter vehicle type: ")
        self.vehilceData()
        
        
    def printCarData(self):
        print("Make year: ", self.makeyear)
        print("Vehicle type: ", self.vehtype)
        
        

car = Car() #car class default constructor
car.getCarData()
car.printCarData()