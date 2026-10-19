# equation is 2x^2 - 5x - 12 = 0
# quadratic formula 
from math import sqrt

a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

discriminant = (b**2) - (4*a*c)
sol1 = (-b - sqrt(discriminant) / (2*a))
sol2 = (-b + sqrt(discriminant) / (2*a))

print(f"The solutions are {sol1} and {sol2}")
