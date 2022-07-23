class Shape: 
    def __init__(self, base, height):
        self.base = base
        self.height = height 
    def area(self): 
        print("I am area of Shape class")

class Triangle(Shape): 
    def areaOfTriangle(self): 
        area = 0.5 * self.base * self.height 
        print("Area is: ", area) 

class Rectangle(Shape): 
    def areaOfRectan(self): 
        area2 = self.base * self.height
        print("Area is: ", area2) 

ob1 = Triangle(4, 5) 
ob1.areaOfTriangle()
ob2 = Rectangle(4, 5)
ob2.areaOfRectan()  