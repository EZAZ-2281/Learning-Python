class Computer:

    def __init__(self):
        self.price = 900

    def sell(self):
        print("Selling Price: {}".format(self.price))
    
    def setPrice(self, pri): 
        self.price = pri 

c = Computer()
c.sell() # 900

# change the price
c.price = 1000
c.sell() # 1000

#using setter method
c.setPrice(2000)
c.sell() # 2000