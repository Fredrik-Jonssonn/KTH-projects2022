# Fredrik Jonsson, grudat22 uppgift 1.1

def factorial(n):
    """Returns the factorial of the non-negative integer n.
    Returns None if n is not a non-negative integer."""
    if isinstance(n, int) and n >= 0:
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return fact
    return None


# Unit Test
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(10) == 3628800
assert factorial(-1) is None
assert factorial(2.33) is None
assert factorial("Hello World") is None
