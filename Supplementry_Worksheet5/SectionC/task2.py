email = input("Please input your email: ").partition("@")

if "@" in email[1] and "." in email[2]:
    print("Email is valid")
else:
    print("Email is invalid")