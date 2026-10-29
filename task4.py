import random

def randomrange(minrange: int, maxrange: int):
    random_number = random.randint(minrange, maxrange)
    return random_number

user_min_number = int(input("Please choose miniumum number: "))
user_max_number = int(input("Please choose maxiumum number: "))

print("Result:", randomrange(user_min_number, user_max_number))