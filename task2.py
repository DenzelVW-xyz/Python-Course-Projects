age = int(input("Input your age: "))

car_type = input("Enter the type of car you want to rent: (Economy, Standard, Luxury): ").lower()

if age < 25 and car_type == "luxury":
    print("Sorry, you are not eligible")
else:
    print("Rent approved")