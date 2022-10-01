n = int(input())
item = []
power = 0

while n >= 2 ** power: 
    item.append(power) 
    power = power + 1

while len(item) != 1: 
    item.pop(0) 

power = power - 1
print(item[0], 2 ** power) 