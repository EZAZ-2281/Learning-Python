def unique_list(l):
  list1 = []
  for a in l:
    if a not in list1:
      list1.append(a)
  return list1 

print(unique_list([1,2,3,3,3,3,4,5])) 
