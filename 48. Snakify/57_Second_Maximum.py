x = int(input())
item = []
flag = 0

while x != 0:
  item.append(x)
  x = int(input())

item.sort()
print(item[len(item)-2])