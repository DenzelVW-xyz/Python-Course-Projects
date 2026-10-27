a, b = 0, 1

for i in range(50):
    print(a, end=", ")
    a, b = b, a + b
    