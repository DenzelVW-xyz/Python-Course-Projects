import random

sentences = input("Input multiple sentences: ").split(". ")

choice = random.choice(sentences)

if choice[-1] != ".":
    choice += "."
    
print(choice)