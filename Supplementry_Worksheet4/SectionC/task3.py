import random

lower_case = lambda: random.choice(list("abcdefghijklmnopqrstuvwxyz"))
upper_case = lambda: random.choice(list("abcdefghijklmnopqrstuvwxyz".upper()))
digits = lambda: random.choice(list("1234567890"))

characters = ["lower_case", "upper_case", "digit"]

def generate_password(length):
    password = ""
    for _ in range(length):
        choice = random.choice(characters)
        if choice == "lower_case":
            password += lower_case()
        elif choice == "upper_case":
            password += upper_case()
        elif choice == "digit":
           password += digits()
    return password

print(generate_password(32))