import random

space_seperated_list = input("Input list seperated by spaces: ").split()
random_word = random.choice(space_seperated_list)

print(random_word)