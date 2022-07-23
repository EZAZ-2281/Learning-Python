import re

pattern = r"Color"

if re.search(pattern, "A Color is beautyful. I love red color"): 
    print("Mathced")
else: 
    print("Not Matched")