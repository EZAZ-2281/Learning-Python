def func(id, name):
    print(id, name)


func(id=12, name="kibria")
#########

#works like dictionary
def func(**details):
    print(details)
    #print(details["id"])


func(id=12, name="kibria")
