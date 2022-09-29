s = input()

if "f" not in s:
  print("")
elif (s.index('f')!= s.rindex('f')):
  print(s.index('f'))
  print(s.rindex('f'))
else:
  print(s.index('f'))
