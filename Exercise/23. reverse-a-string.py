def reverse(name): 
    str = ""
    for x in name: 
        str = x + str 
    return str 

name = input("Enter your name: ")
result = reverse(name) 
print(result) 