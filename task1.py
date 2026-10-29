def right_justify(string: str):
    rightstring = ' ' * 100 + string
    return rightstring

user_string = input("Input your string: ")

print(right_justify(user_string))