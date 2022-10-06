item = [int(i) for i in input().split()]
for i in range(len(item)-1): 
    if(item[i] < item[i+1]): 
        print(item[i+1],end=" ")
    else: 
        continue