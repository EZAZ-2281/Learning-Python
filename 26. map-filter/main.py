def square(x): 
    return x * x
num = [1, 2, 3, 4, 5]

result = list(map(square, num))
#result = list(map(lambda x: x * x, num))
print(result) 
##########
num2 = [1, 2, 3, 4, 5]
res = list(filter(lambda x: x % 2 == 0, num2))
print(res) 