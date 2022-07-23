from abc import ABC, abstractmethod


class Shape(ABC): 
    def __init__(self, base, height):
        self.base = base
        self.height = height 
    
    @abstractmethod
    def area(self): 
        pass

class Triangle(Shape): 
    def area(self): 
        area1 = 0.5 * self.base * self.height 
        print("Area is: ", area1) 

class Rectangle(Shape): 
    def area(self): 
        area2 = self.base * self.height
        print("Area is: ", area2) 

#we can not create a object of Shape class cause its a abstruct class
ob1 = Triangle(4, 5) 
ob1.area()
ob2 = Rectangle(4, 5)
ob2.area()  