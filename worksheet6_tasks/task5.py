import random

alphabet = list("abcdefghijklmnopqrstuvwxyz")

def randomletter():
    chosen_letter = random.choice(alphabet).upper()
    return(chosen_letter)

print("Chosen Letter:", randomletter())