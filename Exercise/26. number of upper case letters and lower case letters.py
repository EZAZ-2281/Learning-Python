str = input("Enter your name: ")
count = 0
count2 = 0
for i in range(len(str)): 
    if(str[i] >= 'a' and str[i] <= 'z'): 
        count = count + 1
    elif(str[i] >= 'A' and str[i] <= 'Z'): 
        count2 = count2 + 1
    else: 
        pass 

print("No of uppercase letter: ", count2)
print("No of lowercase letter: ", count)