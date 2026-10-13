# Define Variables

# Ask user to input the price and calculate then store the discounted price.
laptopPrice = float(input("Please enter the price of the laptop: "))
discountedPrice = (laptopPrice - (0.15 * laptopPrice) - 45)

# Output final price and round to 2 decimal places.
print(f"Your laptop would cost €{round(discountedPrice, 2)} with the discount.")