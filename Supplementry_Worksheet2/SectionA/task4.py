username = "admin"
password = "password123"

user_attempt = input("Enter Your Username: ")
password_attempt = input("Enter Your Password: ")

if user_attempt == username and password_attempt == password:
    print("Login Successful!")
else:
    print("Login Failed.")