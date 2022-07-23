import re
#suru hoby c diye r ses hoby r diye
pattern = r"^color$"
#pattern = r"^col.r$" #matched

if re.match(pattern,"color"): 
    print("Matched")


pattern2 = r"a*" #* means 0 or many output: matched
#pattern2 = r"(ab)*"
if re.match(pattern2, "werwerewr"): 
    print("Matched")

pattern3 = r"a" #+ means 1 or many output: black
#pattern2 = r"a + b*"
if re.match(pattern3, "werwqr"): 
    print("Matched")

pattern4 = r"ice(-)?cream" #? means o or 1
if re.match(pattern4, "icecream"): 
    print("Matchedd")

pattern5 = r"a{1,3}$" #orthat minimum 1 ta r maximum 3 ta a raka jaby
if re.match(pattern5, "aaa"): 
    print("Matcheda")

pattern6 = r"[aeiou]"
if re.match(pattern6, "afsdasdfksadio"): 
    print("Matcheds")

pattern7 = r"[a-z][A-Z][0-9]"
if re.match(pattern7, "aS4fsdasdfksadio"): 
    print("Matchedss")