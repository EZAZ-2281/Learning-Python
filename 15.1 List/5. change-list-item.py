thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
###

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
###

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#['apple', 'blackcurrant', 'watermelon', 'cherry']
###

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#['apple', 'watermelon']
#If we insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
###

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)