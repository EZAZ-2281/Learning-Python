print(bool("kibria")) #true
print(bool(10)) #true
print(bool(["kibria", "rahim"])) #true
"""
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""

"""
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
"""

x = 100
print(isinstance(x, int)) #true

"""function can return a boolean"""
def myFunc(): 
    return True
if myFunc(): 
    print("Its return true")
else: 
    print("nothing")