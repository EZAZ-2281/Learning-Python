item = ["Mike", "", "Emma", "Kelly", "", "Brad"]
a = ""
for i in range(len(item)): 
    if a in item: 
        item.remove(a)

print(item) 