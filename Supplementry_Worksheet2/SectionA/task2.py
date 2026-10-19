num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
operator = input("Input the operator (+, -, /, *): ").strip()

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("invalid operator")

