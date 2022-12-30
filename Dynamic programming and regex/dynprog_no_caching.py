# Fredrik Jonsson, grudat22

def max_income(n, h):
    """Return the max income attainable from n meters of yarn,
    where h is a list of length larger than or equal to (n + 1)
    containing the maximum prices of scarfs i.e. satisfies
    h[0] = 0, and h[k] = ("maximum price of a scarf made
    from k meters of yarn") >= 0. The numbers n and k are
    non-negative integers."""
    curr_max_income = 0
    for i in range(1, n + 1):
        temp = h[i] + max_income(n - i, h)
        if temp > curr_max_income:
            curr_max_income = temp
    return curr_max_income


# Unit Test
def main():
    h_1 = [0, 2, 5, 6, 9, 0, 0, 0, 0]
    assert max_income(5, h_1) == 12
    assert max_income(4, h_1) == 10
    assert max_income(3, h_1) == 7
    assert max_income(2, h_1) == 5
    assert max_income(1, h_1) == 2
    assert max_income(0, h_1) == 0

    h_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert max_income(5, h_2) == 0
    assert max_income(4, h_2) == 0
    assert max_income(3, h_2) == 0
    assert max_income(2, h_2) == 0
    assert max_income(1, h_2) == 0
    assert max_income(0, h_2) == 0

    h_3 = [0, 1000, 3, 4, 6, 7, 200, 0, 0]
    assert max_income(5, h_3) == 5000
    assert max_income(4, h_3) == 4000
    assert max_income(3, h_3) == 3000
    assert max_income(2, h_3) == 2000
    assert max_income(1, h_3) == 1000
    assert max_income(0, h_3) == 0


if __name__ == '__main__':
    main()
