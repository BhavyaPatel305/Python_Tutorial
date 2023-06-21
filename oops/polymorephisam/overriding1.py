#overriding : parent class mehod created in child class with same signature it is called overriding
#singnature means method name and parameter, 
class Gov():
    
    def taxBody(self):
        print("Tax body is GST")


class Person(Gov):
    
    #overriding
    def taxBody(self):
        super().taxBody()
        print("Tax body is Income tax")   



p = Person()
p.taxBody()             