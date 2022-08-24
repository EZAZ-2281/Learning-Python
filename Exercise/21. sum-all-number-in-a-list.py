def findSum(num): 
    total = 0
    for x in num: 
        total = total + x 
    return total 

# sum = findSum(1, 2, 3, 4, 5) 
print(findSum((1, 2, 3, 4, 5))) 