import re

pattern = r"Colour"
text = "This is my favourity Colour, i love this Colour"

ans = re.sub(pattern, "Color", text) 
#ans = re.sub(pattern, "Color", text, count=1) 
print(ans) 