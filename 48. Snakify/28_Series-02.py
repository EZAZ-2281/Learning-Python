a = int(input())
b = int(input())

if(a <= b): 
    count = 1
else: 
    count = -1

for i in range(a, count+b, count): 
    print(i) 