x = int(input())
item = []
flag = 0

while x != 0:
  item.append(x)
  x = int(input())

for i in range(1,len(item)):
  if item[i] > item[i-1]:
    flag += 1
    
print(flag)

