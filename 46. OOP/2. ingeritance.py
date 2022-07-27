class Person: 
    def __init__(self): 
        print("Inside Person class")
    def func1(self): 
        print("I am func1")
    def func2(self): 
        print("I am func2")

class Kibria(Person):
    def __init__(self):
        # super().__init__()
        print("Inside Person class") 
    def func2(self): 
        print("I am inside Kibria class")

obj = Kibria()
obj.func1()
obj.func2() 