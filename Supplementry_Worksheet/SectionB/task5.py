numbers = []

for i in range(4):
    i += 1
    numbers.append(int(input(f"Please enter your {i} number: ")))

print(f"The average of {numbers} is { (sum(numbers)/len(numbers)) }")