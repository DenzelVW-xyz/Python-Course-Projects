menu = {
    1 : "Pizza",
    2 : "Burger",
    3 : "Salad"
}

choice = int(input("Please input an item (1 for pizza, 2 for burger, 3 for salad): "))

if choice == 1:
    print(f"Your item is: {menu[1]}")
elif choice == 2:
    print(f"Your item is: {menu[2]}")
elif choice == 3:
    print(f"Your item is: {menu[3]}")
else:
    print("Invalid Choice")
    

# Note: The reason we are using numbers here is because it would be faster then using strings.