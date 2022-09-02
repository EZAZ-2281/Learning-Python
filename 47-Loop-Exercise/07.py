n = 5
k = 5
for i in range(n + 1): 
    for j in range(k - i, 0, -1): 
        print(j, end=" ")
    print("")