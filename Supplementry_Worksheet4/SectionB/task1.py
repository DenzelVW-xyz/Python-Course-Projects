def calculate_tax(income):
    if income <= 10000:
        tax = 5
    elif income > 10000 and income <= 50000:
        tax = 10
    elif income > 50000:
        tax = 20
    return tax / 100

