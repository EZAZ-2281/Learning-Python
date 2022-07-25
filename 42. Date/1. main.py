from datetime import datetime


a = datetime.now()
print(a) 
x = a.strftime("%I")
y = a.strftime("%M")
z = (x +":"+ y)
print(a.strftime("%a")+",", a.strftime("%b"), a.strftime("%d"), a.strftime("%Y")+".",z ,  a.strftime("%p"))
#Mon, Jul 25 2022. 10 07 pm