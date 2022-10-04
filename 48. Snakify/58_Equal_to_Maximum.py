x = int(input())
item = []
flag = 1

while x != 0:
  item.append(x)
  x = int(input())

max_number = max(item) 
for i in range(len(item)): 
    if(item[i] == max_number): 
        flag = flag + 1

print(flag-1) 