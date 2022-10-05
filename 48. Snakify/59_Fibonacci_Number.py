x = int(input())
item = [1, 1]

if x == 0:
    print(0)
else:
    for i in range(2, x):
        item.append(item[-1] + item[-2])

    print(item[x-1])
