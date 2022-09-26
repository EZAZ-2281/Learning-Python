n = int(input("N: "))
item = []
c = 0
qub = 0
for i in range(1, n+1): 
    c = i
    qub = i * i * i
    item.append(qub)
res = sum(item) 
print(res)