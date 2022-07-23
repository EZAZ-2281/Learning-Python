class Student:
    name = ""
    id = ""

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"Name is: {self.name} and id is: {self.id}")

ob1 = Student("Kibria", 10)
ob1.display()
ob2 = Student("Rahim", 12)
ob2.display()