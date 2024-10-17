def minOperations(n):
    # If n is less than or equal to 1, no operations can be performed to reach n H's
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Factorize n and sum the factors
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
