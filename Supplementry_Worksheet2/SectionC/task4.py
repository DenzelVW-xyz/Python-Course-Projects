length1 = float(input("Enter the first length: "))
length2 = float(input("Enter the second length: "))
length3 = float(input("Enter the third length: "))

if length1 == length2 == length3:
    print("The triangle is Equilateral")
elif length1 == length2 or length2 == length3 or length1 == length3:
    print("The triangle is Isosceles")
else:
    print("The triangle is Scalene")
