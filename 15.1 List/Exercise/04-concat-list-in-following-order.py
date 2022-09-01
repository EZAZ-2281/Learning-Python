from logging import logThreads


list_one = ["Hello ", "take "]
list_two = ["Dear", "Sir"]
list_three = []

for i in range(2): 
    for j in range(2): 
        list_three.append(list_one[i]+list_two[j])

print(list_three) 