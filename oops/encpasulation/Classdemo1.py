class Student:
    
    name = "Parth" # class variable, instance variable
    #self -> keyword, it is a reference variable which is always pointing to current object
    def test(self):
        return "testing.."
    
    def getStudentData(self):
        name = "amit" # local variable
        print("I am a student")
        #witout self keyword, we can not access class variable
        print(self.name)
        print(name)
        self.test()
        #print(name)
        

#how to create an object ?????

stu = Student() # object creation
print(stu.name)
stu.getStudentData()
#stu.test() ---> self

        
    
    
    