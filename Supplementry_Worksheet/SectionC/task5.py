# Company Revenue is R(x) = 4x^2 + 10x + 8 where x is the number of products

products_sold = int(input("Input the number of items sold: "))
total_revenue = 4*products_sold**2 + 10*products_sold + 8

print(f"The total revenue for selling {products_sold} products is {total_revenue}")