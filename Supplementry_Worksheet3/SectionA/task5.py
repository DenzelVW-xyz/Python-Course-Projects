number = int(input("What time table would you like to view?: "))

for i in range(0, 13):
    print(f"{i} X {number} = {i * number}")