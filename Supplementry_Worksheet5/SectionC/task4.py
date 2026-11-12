import random

word = input("What is your word: ")
first_letter = word[0]
last_letter = word[-1]
letters_in_between = list(word[1:-1])

shuffled_letters = ""

while letters_in_between:
    random_letter = random.choice(letters_in_between)
    shuffled_letters += random_letter
    letters_in_between.remove(random_letter)
    
result = first_letter + shuffled_letters + last_letter

print(result)