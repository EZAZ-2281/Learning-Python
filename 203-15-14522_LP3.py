""" class Value():
    x = 5
a = Value()
print(a.x)  """
""" class Person(): 
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age 
ob = Person('rahim',20) 
print(ob.name) 
print(ob.age)  """
""" from unicodedata import name


class Person():
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return f'{self.name} {self.age}'
ob = Person('rahim',20)
print(ob)  """
from unicodedata import name


""" class Person():
    def __init__(self,name,age) -> None:
        self.name = name 
        self.age = age
    def myFunc(self): 
        print(f'My name is: {self.name}')
ob = Person('rahim',20) 
ob.myFunc() """

# Name: Golam Kibria
# S_ID: 203-15-14522

class Student: 
    def __init__(self, n1, id1, n2, id2):
        self.n1 = n1
        self.id1 = id1
        self._n2 = n2 
        self._id2 = id2      

    def display(self):
        print('stu_1 details:')
        print('stu_1 is a student')
        print(f'Name is: {self.n1}')
        print(f'ID is: {self.id1}')
        print('stu_2 details:')
        print('stu_2 is a student')
        print(f'Name is: {self._n2}')
        print(f'ID is: {self._id2}')


n1 = input("Enter stu_1 name: ")
id1 = int(input("Enter stu_1 id: "))
n2 = input("Enter stu_2 name: ")
id2 = int(input("Enter stu_2 id: "))

p = Student(n1, id1, n2, id2) 
p.display()

""" Output: 
Enter stu_1 name: shakib
Enter stu_1 id: 75
Enter stu_2 name: musfiqur
Enter stu_2 id: 15
stu_1 details:
stu_1 is a student
Name is: shakib
ID is: 75


stu_2 details:
stu_2 is a student
Name is: musfiqur
ID is: 15 """