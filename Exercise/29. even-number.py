def find(n): 
    arr = [] 
    for x in n: 
        if x % 2 == 0: 
            arr.append(x) 
    return arr 

print(find([1, 2, 3, 4, 5, 6]))