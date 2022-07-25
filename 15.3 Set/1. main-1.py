num = {1, 2, 3, 4, 5}
print(num)
print(type(num)) #set

num.add(7)
print(num)

num.remove(7)
print(num)

print(4 in num) #true
print(5 not in num) #false

#convert list to set
num2 = set([12, 13, 23, 34])
print(type(num2))