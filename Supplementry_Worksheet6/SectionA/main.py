# Task 1
grocery_list = []
times = 0

while times < 5:
    times = int(input("How many items would you like to add? (Miniumum 5): "))

for i in range(times):
    item = input(f"Items {i + 1}: ")
    grocery_list.append(item)

print(grocery_list)

# Task 2

grocery_list.append("Bread")
print(grocery_list)
item_to_remove = input("What item would you like to remove?: ")
grocery_list.remove(item_to_remove)
print(grocery_list)

# Task 3

print(len(grocery_list))

# Task 4

favorite_colors = []

for i in range(3):
    color = input(f"What is your #{i + 1} favorite color?: ")
    favorite_colors.append(color)

print(f"Your #2 favorite color is {favorite_colors[1]}")

# Task 5

grocery_list.extend(favorite_colors)
combined_list = grocery_list

for element in combined_list:
    print(element)
    
# Task 6

repeat_list = ((input("What is your favorite fruit?: ") + ' ') * 3).split()

for fruit in repeat_list:
    print(fruit)

# Task 7 
print(f"{repeat_list[0]}\n{repeat_list[-1]}")



