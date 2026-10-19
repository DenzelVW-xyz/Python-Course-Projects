# I = PTR

x = float(input("Input the amount of money loaned to you: "))
y = float(input("Input the interest rate: "))
z = int(input("Input the years: "))
amountOwed = x * (1 + y)**z

print(f"After {z} years, you owe {amountOwed}")