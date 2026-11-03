user_birth_year = int(input("When were you born?: "))

def calculate_age(birth_year):
    return 2023 - birth_year

print(f"You are {calculate_age(user_birth_year)} years old.")
    