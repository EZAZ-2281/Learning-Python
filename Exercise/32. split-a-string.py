""" a = input("Enter name: ")
arr = []
for i in a.split('-'): 
     arr.append(i)

arr.sort()
for i in range(len(arr)): 
    print(arr[i],end="-")
    # print('-'.join(arr[i]))  """

item = [i for i in input().split('-')]
item.sort()
print('-'.join(item)) 