s = input()

if "f" not in s:
  print("-2")
elif s.count('f') == 1:
  print ("-1")
else:
  for i in range (s.index('f')+1,len(s)):
    if s[i] == 'f':
      print(i)
      break
  