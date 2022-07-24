fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new = []

for x in fruits: 
    if "a" in x: 
        new.append(x) 
print(new) 

#whitout for loop
#syntax: newlist = [expression for item in iterable if condition == True]
new = [x for x in fruits if "a" in x]
print(new)
new = [x for x in fruits if x != "apple"]
print(new)
new = [x for x in fruits]
print(new) #while list
##################################

result = [x for x in range(10)]
print(result)
result = [x for x in range(10) if x < 5]
print(result) 
#################################
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)