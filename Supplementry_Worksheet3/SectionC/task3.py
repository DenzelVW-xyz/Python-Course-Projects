def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

found_prime_numbers = []
number = int(input("Up to what number would you like to check to: ").strip())

for i in range(number + 1):
    if is_prime(i):
        found_prime_numbers.append(i)
        print(i, end=' ')
        
print("\n")
print(f"The Sum of all the prime numbers found are {sum(found_prime_numbers)}")