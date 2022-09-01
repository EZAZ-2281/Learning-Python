from dataclasses import replace


item = [5, 10, 15, 20, 25, 50, 20]

index = item.index(20) 

item[index] = 200
print(item) 