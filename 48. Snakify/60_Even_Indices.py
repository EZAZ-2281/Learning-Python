s = input()
numbers = list(map(int, s.split()))
item = []
n = 0
while n <= len(numbers)-1:
  item.append(numbers[n])
  n = n + 2
print(str(item).replace(',','').replace('[','').replace(']',''))