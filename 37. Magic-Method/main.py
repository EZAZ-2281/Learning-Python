class Car: 
    def __init__(self, name, color): 
        self.name = name 
        self.color = color 
    
    def __str__(self): 
        return (f"Name is: {self.name} and Color is: {self.color}")

    def __eq__(self, other): 
        return self.name == other.name and self.color == other.color 

    def display(self): 
        print(f"Name is: {self.name} and Color is: {self.color}")

ob1 = Car("Volvo", "White")
ob2 = Car("Volvo", "White")
#ob1.display() 
print(str(ob1))
print(ob1 == ob2) #true 