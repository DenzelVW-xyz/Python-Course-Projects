import random

sentence = input("What is your sentence: ").split()

new_order = []

while sentence:
    selected_word = random.choice(sentence)
    new_order.append(selected_word)
    sentence.remove(selected_word)
    
new_order = " ".join(new_order)

print(new_order)