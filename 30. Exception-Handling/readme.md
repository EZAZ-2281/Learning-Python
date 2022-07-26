```
The try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")
```
```
Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
```
```
In this example, the try block does not generate any error:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
Output: 
Hello
Nothing went wrong
```
```
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

output: 
Something went wrong
The 'try except' is finished
```
```
x = -1
if(x < 0): 
    raise Exception("Sorry, no number below zero")
```
```
x = "Hello"
if not type(x) is int:
    raise Exception("Only integer are allowed")
```