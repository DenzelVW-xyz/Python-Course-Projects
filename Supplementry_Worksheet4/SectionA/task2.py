def calculate_area(length: int, width: int):
    return length * width

user_length = int(input("Input rectangle length: "))
user_width = int(input("Input rectangle width: "))

print("Result:", calculate_area(user_length, user_width) + "Cm^2")