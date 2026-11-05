def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(find_gcd(1000, 700))