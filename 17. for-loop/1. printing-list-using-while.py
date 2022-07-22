from itertools import count


num = [2, 3, 4, 5, 6]
print(num) 

count = 0
length = len(num)
while(count < length):
    print(num[count])
    count = count + 1