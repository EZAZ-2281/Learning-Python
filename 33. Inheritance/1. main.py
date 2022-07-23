class Phone: 
    def call(self): 
        print("Inside Phone class-call")
    def message(self): 
        print("Inside Phone class-message")
class Samsung: 
    #method override call and message
    def call(self): 
        print("Inside Samsung class-call")
    def message(self): 
        print("Inside Samsung class-message")
    def photo(self): 
        print("Inside Samsung class-photo")

ob = Samsung()
ob.call()
ob.message()
ob.photo()