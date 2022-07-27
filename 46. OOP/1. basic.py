class Person: 
    # class attributes
    name = "kibria"

    # instance attributes
    def __init__(this, age, id): 
        this.age = age
        this.id = id 
    
    # instance method
    def address(this, add): 
        return "I live in {} and I am {} years old" .format(add, this.age) 

obj1 = Person(22, 522)

# access the class attributes
# print(obj1.__class__.name) 
print(obj1.name)  

# access_the_instance_attributes
# print(obj1.age, obj1.id) 
print("I am {} years old".format(obj1.age))
print("My id is {}".format(obj1.id)) 

# call our instance method
a = obj1.address("Dhaka")
print(a) 