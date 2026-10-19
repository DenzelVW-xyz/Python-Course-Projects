c = float(input("Input the cost of your item: "))
d = int(input("Input the discount of the item as a %: ")) / 100
cost_after_discount = (c - (c * d))

print(f"After the discount, your item costs {cost_after_discount}")