def multiply(num1: float, num2: float):
    return round(num1 * num2, 2)

usernum1 = float(input("Input your first number: "))
usernum2 = float(input("Input your second number: "))

print("Result:", multiply(usernum1, usernum2))