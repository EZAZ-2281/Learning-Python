item = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_item = ["h", "i", "j"]

item[2][1][2].extend(sub_item)
print(item) 