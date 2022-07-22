book = []
print(type(book)) #list
book.append("rahim")
book.append("karim")
book.append("abdul")
book.append("munna")
print(book)

book.pop()
print(book)
print("The top book is: ", book[-1])
book.pop()
book.pop()
book.pop()
print(book)

if not book: 
    print("No books left")