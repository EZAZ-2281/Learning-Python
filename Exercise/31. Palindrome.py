s = "kibria"
l = len(s)
c = 0
for i in range(l): 
    if(s[i] != s[l-i-1]): 
        c = 1
        break

if c == 0: 
    print("yes")
else: 
    print("Not palindrome")