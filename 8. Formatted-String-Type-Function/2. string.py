"""string are arrays"""
a = "Golam Kibria"
print(a[2])

"""looping through a string"""
a2 = "Kibria"
for x in a2: 
    print(x) 

"""string lenght"""
a3 = "Kibria"
print(len(a3)) #6

"""check string"""
text = "Golam kibria ezaz"
print("kibria" in text) #true
if("kibria" in text): 
    print("Found") 

"""check string"""
text = "Golam kibria ezaz"
print("kibria" not in text) #false
if("kibria" not in text): 
    print("Found") #output nothing