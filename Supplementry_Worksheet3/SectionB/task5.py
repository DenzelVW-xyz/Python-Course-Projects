old_password = "old"
new_password = None

while True:
    user_attempt = input("Enter old password")
    
    if user_attempt != old_password:
        print("Incorrect, Please Try Again.")
        continue
    else:
        print("You guessed correctly, what do you want your new password to be?")
        new_password = input(">>>> ")