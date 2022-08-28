""" name = ["Rahim", "Karim", "abdul", "Billa"]
name.sort(key = str.lower)
print(name)  """

""" num = [1, 2, 3]
num2 = num.copy()
print(num2)  """

""" num = [1, 2, 3]
num2 = list(num) 
print(num2)  """

""" num1 = [1, 2, 3]
num2 = [4, 5, 6]
for x in num2: 
    num1.append(x) 

print(num1)  """


""" num = 28
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
    print("Not a perfect number")   """

""" def isPerfect(n): 
    sum = 0
    for x in range(1, n): 
        if n % x == 0: 
            sum = sum + x 
        
    return sum == n 

print(isPerfect(90)) """

""" s = "kibria"
l = len(s)
c = 0
for i in range(l): 
    if(s[i] != s[l-i-1]): 
        c = 1
        break

if c == 0: 
    print("yes")
else: 
    print("Not palindrome") """


""" a = input("Enter name: ")
arr = []
for i in a.split('-'): 
     arr.append(i)

arr.sort()
for i in range(len(arr)): 
    print(arr[i],end="-")
    # print('-'.join(arr[i]))  """

item = [i for i in input().split('-')]
item.sort()
print('-'.join(item)) 