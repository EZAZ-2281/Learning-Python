def findMax(a, b, c): 
    if(a > b and a > c): 
        largest = a
    elif(b > a and b > c): 
        largest = b 
    else: 
        largest = c
    return largest

large = findMax(4, 8, 2) 

print(large)