import random

rand_number = random.randint(1, 100)

while True:
    user_guess = int(input("Enter a number: "))
    if user_guess == rand_number:
        print("You guessed the number!")
        break
    elif user_guess > rand_number:
        print("Lower")
    else:
        print("Higher")