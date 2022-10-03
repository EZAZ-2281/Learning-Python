sum = 0
flag = 1
c = 0
while flag > 0:
    a = int(input())
    sum = sum + a
    c = c + 1
    if a == 0: 
        print(sum / (c-1)) 
        break

