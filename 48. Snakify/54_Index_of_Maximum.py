x = int(input())
item = []

while x != 0:
  item.append(x)
  x = int(input())

print(item.index(max(item))+1)