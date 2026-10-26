attempts = 5
pin = 1234

while attempts > 0:
    user_pin = int(input("Input your pin: "))
    
    if user_pin == pin:
        print("Withdrawl Successful")
        break
    else:
        attempts -= 1
        print("Invalid pin Please try again")

if attempts < 1:
    print("Ran out of attempts")