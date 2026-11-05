def calculate_factorial(n):
    if n < 0:
        # Number cannot be negative
        raise ValueError
    else:
        answer = 1
        for i in range(1, n+1):
            answer *= i
        return answer
            
print(calculate_factorial(5))
