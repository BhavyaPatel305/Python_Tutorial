class Param():   
    
       
        
    def pop(self, param1, param2):
        print("pop with 2 params called...",param1, param2)

    def pop(self):
        print("pop withput param called...")

    def pop(self, param1):
        print("pop with param called...",param1)

p = Param()
p.pop(12,22)

            