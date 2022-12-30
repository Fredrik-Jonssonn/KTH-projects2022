# Fredrik Jonsson, grudat22 uppgift 3.1

def factorial(n):
    """Return the factorial of the non-negative integer n.
    Return None if n is not a non-negative integer."""
    if type(n) is not int or n < 0:
        return None
    if n == 0:
        return 1
    else:
        fact = n * factorial(n - 1)
    return fact


# Unit Test
def main():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(10) == 3628800
    assert factorial(-1) is None
    assert factorial(2.33) is None
    assert factorial("Hello World") is None


if __name__ == '__main__':
    main()
