c = int(input())
r = int(input())
nc = int(input())
nr = int(input())

if (c == nc or r == nr or abs(c - nc) == abs(r - nr)): 
    print("YES") 
else: 
    print("NO") 