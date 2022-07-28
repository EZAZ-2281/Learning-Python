class Item: 
    payRate = 0.8
    def __init__(this, name:str, price:float, quantity = 0): 
    
        # run validation
        assert price >= 0, f"{price} must be greater than or equal to zero"
        assert quantity >= 0, f"{quantity} must be greater than or equal to zero"

        # assign
        this.name = name 
        this.price = price
        this.quantity = quantity
    
    def result(this): 
        return this.price * this.quantity

    def discount(this): 
        this.price = this.price * this.payRate

item1 = Item("Phone", 100, 5)
item1.discount()
print(item1.price) # 80.0

item2 = Item("Laptop", 200, 5)
item2.payRate = 0.7 # get the value from instance level
item2.discount()
print(item2.price) # 140.0