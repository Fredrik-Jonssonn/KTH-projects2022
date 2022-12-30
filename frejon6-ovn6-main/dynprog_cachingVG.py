# Fredrik Jonsson, grudat22

class ScarfCollection:
    """A scarf collection storing a list of scarfs and the
    collection's value, where the list of scarfs
    self.scarfs satisfies self.scarfs[n] = ("the number of
    scarfs in the collection created from n meters of yarn")
    and that if n is out of bounds the number of scarfs made from
    n meters of yarn is 0. The number n is a non-negative integer."""

    def __init__(self):
        self.scarfs = []  # The list of scarfs
        self.value = 0  # The collections value


def max_value_collection(n, h, memo=[]):
    """Return a max value scarf collection (ScarfCollection object)
    made from n meters of yarn, where h is a list of length
    larger than or equal to (n + 1) containing the maximum prices
    of scarfs i.e. satisfies h[0] = 0, and
    h[k] = ("maximum price of a scarf made from k meters of yarn") >= 0.
    The numbers n and k are non-negative integers."""
    if len(memo) == 0:
        memo = [None for _ in range(n + 1)]
    if memo[n] is not None:
        return memo[n]
    curr_max_value_collection = ScarfCollection()
    curr_max_value_collection.scarfs = [0 for _ in range(n + 1)]
    temp_scarf = None
    for i in range(1, n + 1):
        temp_value = h[i] + max_value_collection(n - i, h, memo).value
        if temp_value > curr_max_value_collection.value:
            curr_max_value_collection.value = temp_value
            temp_scarf = i
    if temp_scarf is not None:
        for i in range(n + 1 - temp_scarf):
            curr_max_value_collection.scarfs[i] = memo[n - temp_scarf].scarfs[i]
        curr_max_value_collection.scarfs[temp_scarf] += 1
    memo[n] = curr_max_value_collection
    return curr_max_value_collection


# Unit Test
def main():
    h_1 = [0, 2, 5, 6, 9, 0, 0, 0, 0]
    assert max_value_collection(5, h_1).value == 12
    assert max_value_collection(5, h_1).scarfs == [0, 1, 2, 0, 0, 0]
    assert max_value_collection(4, h_1).value == 10
    assert max_value_collection(4, h_1).scarfs == [0, 0, 2, 0, 0]
    assert max_value_collection(3, h_1).value == 7
    assert max_value_collection(3, h_1).scarfs == [0, 1, 1, 0]
    assert max_value_collection(2, h_1).value == 5
    assert max_value_collection(2, h_1).scarfs == [0, 0, 1]
    assert max_value_collection(1, h_1).value == 2
    assert max_value_collection(1, h_1).scarfs == [0, 1]
    assert max_value_collection(0, h_1).value == 0
    assert max_value_collection(0, h_1).scarfs == [0]

    h_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert max_value_collection(5, h_2).value == 0
    assert max_value_collection(5, h_2).scarfs == [0, 0, 0, 0, 0, 0]
    assert max_value_collection(4, h_2).value == 0
    assert max_value_collection(4, h_2).scarfs == [0, 0, 0, 0, 0]
    assert max_value_collection(3, h_2).value == 0
    assert max_value_collection(3, h_2).scarfs == [0, 0, 0, 0]
    assert max_value_collection(2, h_2).value == 0
    assert max_value_collection(2, h_2).scarfs == [0, 0, 0]
    assert max_value_collection(1, h_2).value == 0
    assert max_value_collection(1, h_2).scarfs == [0, 0]
    assert max_value_collection(0, h_2).value == 0
    assert max_value_collection(0, h_2).scarfs == [0]

    h_3 = [0, 1000, 3, 4, 6, 7, 200, 0, 0]
    assert max_value_collection(5, h_3).value == 5000
    assert max_value_collection(5, h_3).scarfs == [0, 5, 0, 0, 0, 0]
    assert max_value_collection(4, h_3).value == 4000
    assert max_value_collection(4, h_3).scarfs == [0, 4, 0, 0, 0]
    assert max_value_collection(3, h_3).value == 3000
    assert max_value_collection(3, h_3).scarfs == [0, 3, 0, 0]
    assert max_value_collection(2, h_3).value == 2000
    assert max_value_collection(2, h_3).scarfs == [0, 2, 0]
    assert max_value_collection(1, h_3).value == 1000
    assert max_value_collection(1, h_3).scarfs == [0, 1]
    assert max_value_collection(0, h_3).value == 0
    assert max_value_collection(0, h_3).scarfs == [0]


if __name__ == '__main__':
    main()
