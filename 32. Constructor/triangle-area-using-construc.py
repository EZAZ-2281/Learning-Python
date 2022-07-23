class Triangle: 
    base = ""
    height = "" 

    def __init__(self, base, height): 
        self.base = base
        self.height = height
    
    def display(self):
        area = 0.5 * self.base * self.height
        print("The area of triangle is: ", area) 

ob = Triangle(2, 3)
ob.display() 

ob1 = Triangle(4, 5)
ob1.display() 