class Phone: 
    def call(self): 
        print("Inside Phone class-call")
    def message(self): 
        print("Inside Phone class-message")
class Samsung(Phone): 
    #call and message
    def photo(self): 
        print("Inside Samsung class-photo")

ob = Samsung()
ob.call()
ob.message()
ob.photo()
print(issubclass(Samsung, Phone)) #true
#phone holo super or parent or base class