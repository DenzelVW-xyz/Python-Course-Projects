# Variables

amountOfBooks = int(input("How Many Books: "))
coverPrice = 25
bookstoreDiscount = (coverPrice - (coverPrice * float(0.40)))
shipping = 3
additionalCopy = float(0.75)

print((amountOfBooks * bookstoreDiscount) + shipping + ((amountOfBooks - 1) * additionalCopy))