class Item: 
    payRate = 0.8
    all = []
    def __init__(this, name:str, price:float, quantity = 0): 
    
        # run validation
        assert price >= 0, f"{price} must be greater than or equal to zero"
        assert quantity >= 0, f"{quantity} must be greater than or equal to zero"

        # assign
        this.name = name 
        this.price = price
        this.quantity = quantity

        # action to exucute
        Item.all.append(this) 
    
    def result(this): 
        return this.price * this.quantity

    def discount(this): 
        this.price = this.price * this.payRate

    def __repr__(this): # how to represent the object
        return f"Item({this.name}, {this.price}, {this.quantity})"

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 100, 5)
item3 = Item("Mouse", 100, 5)
for x in Item.all: 
    print(x.name) 

print(Item.all) 
