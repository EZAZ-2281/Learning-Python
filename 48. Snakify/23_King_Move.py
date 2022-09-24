c = int(input())
r = int(input())
nc = int(input())
nr = int(input())

if(c == nc or c == nc + 1 or c == nc - 1) and (r == nr or r == nr + 1 or r == nr - 1): 
    print("YES")
else: 
    print("NO") 