def minOperations(n):
    # If n is less than or equal to 1, no operations are needed
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2  # Start checking from the smallest prime factor
    
    # Loop until n is reduced to 1
    while n > 1:
        # If n is divisible by the current divisor, keep dividing
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        # Move to the next divisor
        divisor += 1
    
    return operations

