class Item: 
    def res(self, x, y): 
        return x * y 

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.res(item1.price, item1.quantity))