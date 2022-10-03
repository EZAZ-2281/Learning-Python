x = int(input())
item = []
i = 0
c = 0
while x != 0:
    item.append(x)
    x = int(input())

    if (item[i] % 2 == 0):
        c = c + 1
    i = i + 1

print(c)
