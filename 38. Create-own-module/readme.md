```
import mymodule as mx

a = mx.person1["age"]
print(a)
```
```
Example
The module named mymodule has one function and one dictionary:

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
Example
Import only the person1 dictionary from the module:

from mymodule import person1

print (person1["age"])
```
```
Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]
```