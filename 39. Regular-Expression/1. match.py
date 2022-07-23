import re

pattern = r"Color"

if re.match(pattern, "Color is beautyful. I love red color"): 
    print("Mathced")
else: 
    print("Not Matched")