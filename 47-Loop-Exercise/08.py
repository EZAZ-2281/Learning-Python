list1 = [10, 20, 30, 40, 50]
# list1.sort(reverse=True)
# print(list1) 

size = len(list1) 

for i in range(size-1, -1, -1): 
    print(list1[i], end=" ")

print("\n")
nlist = reversed(list1) 
for i in nlist: 
    print(i, end=" ") 