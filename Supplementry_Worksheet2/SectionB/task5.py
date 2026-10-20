days_overdue = int(input("Input how many days book is overdue: "))

if days_overdue <= 20:
    late_fee = days_overdue * 0.25
elif days_overdue <= 40:
    late_fee = 20 * 0.25 + (days_overdue - 20) * 0.50
else:
    late_fee = 20 * 0.25 + 20 * 0.50 + (days_overdue - 40)
    
    
print(f"The late fee is: {late_fee}")