class Student: 
    name = "" 
    id = ""

    def display(self):
        print(f"Name is: {self.name} and ID is: {self.id}") 

ob1 = Student()
ob1.name = "kibria"
ob1.id = "10"
ob1.display() 

ob2 = Student()
ob2.name = "Rahim"
ob2.id = "12"
ob2.display() 