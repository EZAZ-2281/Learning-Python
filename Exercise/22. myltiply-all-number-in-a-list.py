def multiple(num): 
    multi = 1
    for x in num: 
        multi = multi * x
    return multi 

ans = multiple(((8, 2, 3, -1, 7)))
print(ans) 