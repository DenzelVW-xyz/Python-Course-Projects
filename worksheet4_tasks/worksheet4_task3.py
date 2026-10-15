while True:
    number = int(input("Input a number to check if its even: "))
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")