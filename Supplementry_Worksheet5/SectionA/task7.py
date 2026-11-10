vowels = 'aeiou'
sentence = input("Input sentence: ")
total = 0
total = sum(total + 1 for letter in sentence if letter.lower() in vowels)

print(total)
