hour = int(input())
minute = int(input())
second = int(input())

r1 = hour * 30
r2 = minute * 30 / 60
r3 = second * 30 / 3600

print(r1+r2+r3) 