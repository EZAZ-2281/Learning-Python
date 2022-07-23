class A: 
    def display(self): 
        print("I am inside A class")
class B: 
    def display(self): 
        print("I am inside B class")
class C(A, B): 
    def display(self): 
        print("I am inside C class")

ob = C()
ob.display() 


"""
class A: 
    def display(self): 
        print("I am inside A class")
class B: 
    def display(self): 
        print("I am inside B class")
class C(A, B): 
    pass

ob = C()
ob.display() #I am inside A class because C(A, B) A is first
"""