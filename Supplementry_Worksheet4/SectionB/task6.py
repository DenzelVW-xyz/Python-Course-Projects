def convert_temperature(degrees: float, scale: str):
    if scale.upper() == "F":
        return (degrees * 9/5) + 32
    elif scale.upper() == "C":
        return (degrees - 32) * 5/9

print(convert_temperature(0, "C")) # convert F to C
print(convert_temperature(0, "F")) # convert C to F

