from random import randint

# Task 1
temperature_log = sorted([randint(1, 100) for _ in range(7)], reverse=True)
print(f"{max(temperature_log)}\n{min(temperature_log)}")

# Task 2
duplicate_list = [1, 1, 2, 2, 2, 4, 4, 6, 5, 5, 8, 8, 8, 9]
removed_duplicates = list(set(duplicate_list))
for element in removed_duplicates:
    print(element)

# Task 3
print(temperature_log[1:5])

# Task 4
random_numbers = sorted([randint(1, 100) for _ in range(10)])
for number in random_numbers:
    print(number)

# Task 5
squared_numbers = [i**2 for i in range(1, 6)]
for number in squared_numbers:
    print(number)

# Task 6
reversed_square_numbers = reversed(squared_numbers)
for number in reversed_square_numbers:
    print(number)

# Task 7
words = ["I", "Really", "Love", "KFC", "Because", "Its", "Yummy"]
new_words = " ".join(words).replace("Yummy", "Amazing").split()
for word in new_words:
    print(word)
