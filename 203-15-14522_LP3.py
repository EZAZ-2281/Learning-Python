student = {}

for i in range(5):
    name = input("Enter student name: ")
    id = input("Enter student's id: ")

    student[name] = id

    # student.update({"name[2]": id[2]+1})
    print(student) 

def countEven(student):      
    even = 0      
    for i in student.values():       
      if i % 2 == 0:
        even = even + 1    
      else: 
        pass      
    print("Total Even ID: ", even)
countEven(student)