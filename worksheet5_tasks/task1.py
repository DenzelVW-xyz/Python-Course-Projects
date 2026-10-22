word = input("What is your word: ")
counter = 0

for letter in word:
    counter += 1
    print(f"Letter #{counter} is: {letter}")
    
    if counter >= 6:
        print("String is too long")
        break
    