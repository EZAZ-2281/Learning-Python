take_number = int(input())
sum = 0
while(take_number > 0): 
    rem = take_number % 10
    sum = sum + rem
    take_number = take_number // 10

print(sum) 