take_input = str(input())
find_space = take_input.find(' ')
print(take_input[find_space:] + " " + take_input[:find_space])