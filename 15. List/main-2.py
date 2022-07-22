name = ["c", "cpp", "java", "python", "js", "css", "html"]

print(len(name))  # 7

name.append("swift")  # for ading item at the end of the list
print(name)

name.insert(2, "carbon")  # carbon will add in 2nd index
print(name)

name.remove("css")
print(name)

name.sort()
print(name)  # we can also sort number as well

name.reverse()
print(name)

name.pop()  # last item which means html will remove/pop up
print(name)

name2 = name.copy()  # for copying the list
print(name2)

pos = name.index("java")  # determine the index number of java
print(pos)  # 3

namee = [2, 3, 4, 4]
counts = namee.count(4)  # return how many time 4 is appear in the list.
print(counts)  # 2

name.clear()
print(name)  # []
