# Count the number of divisors of a positive integer n.
#
# Random tests go up to n = 500000.

def divisors(n):
    return len([i for i in range(1, n + 1) if n % i == 0])