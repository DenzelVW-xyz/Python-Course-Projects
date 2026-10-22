word = "Mellieha"
counter = 0

for letter in word:
    if letter == "l" or letter == "L":
        print("L ecounterd, skipping....")
        continue
    else:
        counter += 1
        print(f"Letter {counter} is {letter}")
    