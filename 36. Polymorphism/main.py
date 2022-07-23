#build in polymorphic function
print(len("Golam kibria"))
print(len([1, 2, 4]))

#user define polymorphic function
def add(a, b, c = 0): 
    return a + b + c

print(add(1, 2, 4))
print(add(1, 2))