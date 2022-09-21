# Taking integer input 
print("Enter the size of the array: ")
n = int(input())
item = []
for i in range(n): 
    num = int(input())
    item.append(num) 

# Function for sort the list 
item.sort()
print(item) 
# Pick the first item from the list 
first_item = item[0]
# Checking the first item if is it divided by 5
if(first_item % 5 == 0): 
    print('Won the Lottery!')
else: 
    print('Kopal tai Kharap')

""" 
Output: 
Enter the size of the array: 
10
12
23
56
20
90
65
35
67
87
12
[12, 12, 20, 23, 35, 56, 65, 67, 87, 90]
Kopal tai Kharap """