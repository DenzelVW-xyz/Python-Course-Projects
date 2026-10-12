# Variables

amountOfBooks = float(input("How Many Books: "))
coverPrice = 25
bookstoreDiscount = (coverPrice - (coverPrice * 0.40))
shipping = 3
additionalCopy = 0.75

print((amountOfBooks * bookstoreDiscount) + shipping + (amountOfBooks * additionalCopy))