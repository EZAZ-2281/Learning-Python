class Phone: 
    def __init__(self): 
        print("I am Phone class")

class Samsung(Phone): 
    def __init__(self):
        super().__init__()
        print("I am Samsung class") 

ob = Samsung() 