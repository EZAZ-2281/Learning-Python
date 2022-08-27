num = 28
num2 = int(num / 2)
# print(num2) 
arr = []
for x in range(1, num2+1): 
    if(num % x == 0): 
        arr.append(x) 

print(arr) 
# arr = [1, 2, 4, 7, 14] 
c = 0
for i in range(len(arr)):
    c = c + arr[i] 

print(c) 
if c == num: 
    print("Its a perfect number") 
else: 
    print("Not a perfect number") 




""" def isPerfect(n): 
    sum = 0
    for x in range(1, n): 
        if n % x == 0: 
            sum = sum + x 
        
    return sum == n 

print(isPerfect(90)) """