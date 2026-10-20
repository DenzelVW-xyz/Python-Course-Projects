weight = float(input("Enter the weight: "))
destination = input("Enter the destination (Domestic or International): ")

if destination == "domestic":
    print(5 + 1 * weight)

elif destination == "international":
    print(10 + 3 * weight)

else:
    print("invalid input")
