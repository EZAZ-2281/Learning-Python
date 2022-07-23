import re

pattern = r"Color"
text = "My favourite Color is red"
res = re.search(pattern, text) 
if res: 
    print(res.start()) #13
    print(res.end()) #18
    print(res.span()) #(13, 18)