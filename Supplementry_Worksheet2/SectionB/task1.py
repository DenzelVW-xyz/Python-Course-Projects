distance = float(input("Input the distance: "))
time = float(input("Input the amount of minutes you took in minutes: "))

if distance <= 5:
    total_cost = 10
elif distance > 5:
    total_cost = 10 + ((distance - 5) * 2)

if time > 30:
    total_cost +=5
    
    
print(f"Your total is {total_cost}")

    
