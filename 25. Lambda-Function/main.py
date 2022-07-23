def calculate(a, b): 
    return a*a + 2 * a * b + b*b 

result = calculate(2, 3) 
print(result) 
######
ans = (lambda a, b: a*a + 2 * a * b + b*b)(2, 3)
print("Using lambda: ",ans) 
######
ans2 = (lambda a: a * a * a)(2) 
print("Cube is: ", ans2) 