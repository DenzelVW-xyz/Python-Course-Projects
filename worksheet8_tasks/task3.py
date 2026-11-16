lstMonths = "January Februrary March April May June July August September October November December".split()
birthmonth = int(input("Enter a number based on birth month: ").strip())
print("The month is:", lstMonths[birthmonth - 1])