old_password = "old"
new_password = None
attempts = 5

while attempts > 0:
    user_attempt = input("Enter old password")
    
    if user_attempt != old_password:
        print("Incorrect, Please Try Again.")
        attempts -= 1
        continue
    else:
        print("You guessed correctly, what do you want your new password to be?")
        new_password = input(">>>> ")