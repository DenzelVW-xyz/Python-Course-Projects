menu = {
    1 : "pizza",
    2 : "Burger",
    3 : "Salad"
}

choice = int(input("Please input an item (1, 2, 3): "))

if choice == 1:
    print(f"Your item is: {menu[1]}")
elif choice == 2:
    print(f"Your item is: {menu[2]}")
elif choice == 3:
    print(f"Your item is: {menu[3]}")
else:
    print("Invalid Choice")