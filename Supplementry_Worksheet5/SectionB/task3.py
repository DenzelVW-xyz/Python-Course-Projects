price = input("Input price: ").partition("€")
price_as_float = round(float(price[2]), 2)

print("Price:", price_as_float)

