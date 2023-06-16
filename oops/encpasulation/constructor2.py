class Shape:
    
    name = None
    size = None
    #circle,Circle, 10
    def __init__(self, name, size):
        #ciricle.name =Circle
        self.name = name
        #ciricle.size = 10
        self.size = size

    def printShape(self):
        print("Shape name is: ", self.name)
        print("Shape size is: ", self.size)
        

circle = Shape("Circle", 10) #circle
square = Shape("Square", 20)
triangle = Shape("Triangle", 30)

circle.printShape()
square.printShape()
triangle.printShape()        

        
        