letter = 0
digit = 0
word = 0

numText = input("Enter text and number: ")

for x in numText: 
    x = x.lower()
    if(x >= 'a' and x <= 'z'):
        letter = letter + 1 
    elif(x >= '0' and x <= '9'):
        digit = digit + 1
    elif(x == " "):
        word = word + 1

print("Number of letter: ", letter) 
print("Number of digit: ", digit) 
print("Number of word: ", word+1) 