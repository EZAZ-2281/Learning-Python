student = {
    "name" : "kibria",
    "id" : 101,
    "add" : "dhaka"
}
print(student["name"])
print(student["id"])
#print(student["names"]) key errors
print(student.get("add"))
print(student.get("names")) #none
print(student.get("names", "Not a valid key"))