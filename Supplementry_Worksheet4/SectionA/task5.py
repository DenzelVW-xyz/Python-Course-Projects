def calculate_discounted_price(original_price, discount_percentage):
    newprice = original_price - (original_price * (discount_percentage / 100))
    return newprice

user_price = float(input("Input the price of the item: "))
user_discount = int(input("Input the discount percentage: "))

print(f"New price {calculate_discounted_price(user_price, user_discount):.2f}")