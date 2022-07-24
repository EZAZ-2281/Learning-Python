a = "kibria"
def func(): 
    print("I am ", a) 

func()
#####
a = "kibria"
def func(): 
    a = "Ezaz"
    print("I am ", a) 

func()
print("I am ", a) 
#####
def func(): 
    global a 
    a = "Ezaz"
    print("I am ", a) 

func()
print("I am ", a) 
#####
a = "Kibria"
def func(): 
    global a 
    a = "Ezaz"
    print("I am ", a) 

func()
print("I am ", a) 
#####