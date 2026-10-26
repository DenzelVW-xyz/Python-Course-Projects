def isprime(number):
    if number == 1:
        return f"{number} is not a prime number"
    else:
        if (number % 1 == 0 and number % number == 0) and (number % 2 == 0):
            return f"{number} is a prime number"
        else:
            return f"{number} is not a prime number"
        
        
while True:
    user_number = int(input("Enter a number: "))
    print(isprime(user_number))
    print((user_number % 1 == 0 and user_number % user_number == 0))
    print((user_number % 2 != 0))
    
# Code above is incorrect due to a logical error