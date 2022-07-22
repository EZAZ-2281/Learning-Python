n = input("Enter text of number: ")
num = n.split()
sum = 0

for x in num: 
    sum = sum + int(x)
print("Sum is: ", sum)