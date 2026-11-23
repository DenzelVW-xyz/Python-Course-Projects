# Task 1
matrix = [["x" for _ in range(3)] for _ in range(3)]
for i in range(len(matrix)):
    print(matrix[i])

# Task 2
daily_schedules = [
    ["Work", "Sleep", "Eat"],
    ["Study", "Sleep", "Eat"],
    ["Work", "Eat", "Sleep"],
]
for schedule in daily_schedules:
    print(schedule)

# Task 3
numbers = [1, 2, 3, 4, 4, 5, 6, 7, 88, 96, 0]
even_only = [num for num in numbers if num % 2 == 0]
for num in even_only:
    print(num)

# Task 4
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8]
list2 = [2, 3, 4, 6, 8, 0]
common = list(
    {item for item in list1 if item in list2}
)  # Set comprehension converted into list to easily remove duplicates.
for item in common:
    print(item)

# Task 5
words = ["Hello", "Chicken", "Banana", "Tree", "So", "Do", "Awe"]
updated_words = [word for word in words if len(word) >= 4]
for word in updated_words:
    print(word)

# Task 6
for row in matrix:
    print(row[1])

# Task 7
names = ["Denzel", "Jean", "Liam", "Jerome", "Jimmy"]
ages = [16, 16, 17, 12, 67]
names_and_ages = list(zip(names, ages))
for pair in names_and_ages:
    print(pair)
split_names_and_ages = list(zip(*names_and_ages))
for lists in split_names_and_ages:
    print(list(lists))
