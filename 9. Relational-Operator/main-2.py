"""
Arithmetic operators
Assignment operators
Comparison operators (==, <, >, <=, >=, !=)
Logical operators (and, or, not)
Identity operators (is,is not)
Membership operators (in, not in)
Bitwise operators
"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list