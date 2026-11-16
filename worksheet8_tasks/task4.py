shoppingList = []

def add(item):
    global shoppingList
    shoppingList.append(item)

def rm(item):
    global shoppingList
    shoppingList.pop(item - 1)

def change():
    global shoppingList
    item_to_change = input("What item would you like to change?: ")
    item_to_replace_with = input("What item would you like to replace it with?: ")
    shoppingList[shoppingList.index(item_to_change)] = item_to_replace_with
    print("Replaced!")

def view():
    global shoppingList
    for number, item in enumerate(shoppingList, start=1):
                print(f"{number}: {item}")

while True:
    print("Press one of the following letters: ")
    print("""
          P. Print List of items to buy
          A. Add Items to the list
          R. Remove Items from the list
          C. Change items from the list
          Q. Quit
          """)
    choice = input("Enter Your Choice: ").strip().upper()
    
    if choice == "P":
        view()
    elif choice == "A":
        times = int(input("How many items would you like to add?: ").strip())
        for _ in range(times):
            item = input("What item to add?: ")
            add(item)
    elif choice == "R":
        view()
        item = int(input("What item to remove?: "))
        rm(item)
    elif choice == "C":
        change()
    elif choice == "Q":
        # Basically exit() or quit() but better
        raise SystemExit(0)
    else:
        print("Invalid Choice")