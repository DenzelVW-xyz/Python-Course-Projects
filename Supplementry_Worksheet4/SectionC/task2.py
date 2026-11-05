def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Quick explaination, to find lcm, you can multiply both numbers together, then divide by the gcd, so a * b / find_gcd(a, b)
def find_lcm(a, b):
    return a * b / find_gcd(a, b)

print(find_lcm(6, 20))