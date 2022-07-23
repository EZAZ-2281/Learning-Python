class Student: 
    name = "" 
    id = ""

    def setValue(self, name, id): 
        self.name = name
        self.id = id 

    def display(self):
        print(f"Name is: {self.name} and ID is: {self.id}") 

ob1 = Student()
ob1.setValue("kibria", 10)
ob1.display() 

ob2 = Student()
ob2.setValue("Rahim", 12)
ob2.display() 