import re

pattern = r"Color"

if re.findall(pattern, "A Colore is beautyful. I love red color"): 
    print("Mathced")
else: 
    print("Not Matched")