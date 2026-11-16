temperatures = [temp for temp in range(1, 100, 10)]

# A)
print(temperatures)
# B)
for temp in temperatures:
    print(temp)
# C)
print([temp for temp in temperatures if temp > 20])
# D)
temperatures.pop(1)
temperatures.pop(2)
print(temperatures)