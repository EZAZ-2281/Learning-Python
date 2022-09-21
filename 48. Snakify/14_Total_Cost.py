total_dollar = int(input())
totoal_cents = int(input())
total_amount = int(input())

res = total_dollar * 100
res2 = res + totoal_cents
res3 = total_amount * res2

print(res3 // 100, res3 % 100) 