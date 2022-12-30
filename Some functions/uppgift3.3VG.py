# Fredrik Jonsson, grudat22 uppgift 3.3

def sign_partition(v):
    """Reorder the elements of the vector v storing numbers (float or int)
    so that the negative elements come first"""
    low, high = 0, len(v)
    while low < high:
        # Invariant:
        # - v[:low] < 0
        # - v[low:high] are unknown
        # - v[high:] >= 0
        #
        #          < 0          unknown         >= 0
        #    ----------------------------------------------
        # v: |              |a             |              |
        #    ----------------------------------------------
        #                    ^              ^
        #                   low            high
        a = v[low]
        if a < 0:
            low += 1
        else:
            v[low] = v[high - 1]
            v[high - 1] = a
            high -= 1


def _sign_partition_test(v):
    """Return True if the vector v storing numbers (float or int) is
    ordered so that the negative elements come first, else return False"""
    non_negative_part = False
    for i in range(len(v)):
        if v[i] >= 0:
            non_negative_part = True
        elif non_negative_part is True:
            return False
    return True


# Unit Test
def main():
    test_vector1 = [-3, 2, -1, 0, 5]
    sign_partition(test_vector1)
    assert all(i in test_vector1 for i in [-3, 2, -1, 0, 5])
    assert len(test_vector1) == 5
    assert _sign_partition_test(test_vector1)

    test_vector2 = [-3.2, 24.5, -1.3, 0.5, 5.4]
    sign_partition(test_vector2)
    assert all(i in test_vector2 for i in [-3.2, 24.5, -1.3, 0.5, 5.4])
    assert len(test_vector2) == 5
    assert _sign_partition_test(test_vector2)

    test_vector3 = [-3.2, 32, -10, 0, 5.4]
    sign_partition(test_vector3)
    assert all(i in test_vector3 for i in [-3.2, 32, -10, 0, 5.4])
    assert len(test_vector3) == 5
    assert _sign_partition_test(test_vector3)

    test_vector4 = [-3]
    sign_partition(test_vector4)
    assert all(i in test_vector4 for i in [-3])
    assert len(test_vector4) == 1
    assert _sign_partition_test(test_vector4)


if __name__ == '__main__':
    main()
