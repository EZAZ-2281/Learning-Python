list_one = [10, 20, 30, 40]
list_two = [100, 200, 300, 400]
n = 3
for i in range(4): 
    print(list_one[i], list_two[n])
    n = n - 1
    if(n < 0): 
        break 