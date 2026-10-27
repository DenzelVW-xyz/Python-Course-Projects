shift = None

while shift is None:
    try:
        shift = int(input("Enter a number between 1 and 25: "))
        if shift > 25 or shift < 1:
            shift = None
            print("Put a number between 1 and 25")
    except ValueError:
        print("Please enter a valid number!")

phrase = input("Please enter the phrase you want to encrypt: ")

character_as_code = []
shifted_string = []

for letter in phrase:
    if 'a' <= letter <= 'z':
        character_as_code.append((ord(letter) - ord('a') + shift) % 26 + ord('a'))
    elif 'A' <= letter <= 'Z':
        character_as_code.append((ord(letter) - ord('A') + shift) % 26 + ord('A'))
    else:
        character_as_code.append(ord(letter))

for number in character_as_code:
    shifted_string.append(chr(number))

print(f"The encrypted phrase is: {''.join(shifted_string)}")