word = input("Enter a word: ")
newword = ""

for letter in word:
    if letter == "l" or letter == "L":
        newword += letter
    else:
        newword += "_"

print(newword)
        