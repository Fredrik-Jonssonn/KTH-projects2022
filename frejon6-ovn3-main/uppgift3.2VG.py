# Fredrik Jonsson, grudat22 uppgift 3.2

def mode(v):
    """Return the mode of the vector v storing integers.
    If two values are equally frequent return the smaller
    value."""
    curr_mode = v[0]
    count_dict = {}
    for i in range(len(v)):
        if v[i] in count_dict:
            count_dict[v[i]] += 1
        else:
            count_dict[v[i]] = 1
    for key in count_dict:
        if (count_dict[key] > count_dict[curr_mode]) or \
                (count_dict[key] == count_dict[curr_mode] and key < curr_mode):
            curr_mode = key
    return curr_mode


# Unit Test
def main():
    assert mode([-2, 2, -1, 0, 1]) == -2
    assert mode([-3, 2, -2, 2, 2]) == 2
    assert mode([0, 0, 1, 1, 1]) == 1
    assert mode([1, 0, 1, 0, 2]) == 0
    assert mode([1, 1, 2, 2, 3, 3]) == 1
    assert mode([1, 2, 6, 2, 7, 3, 2]) == 2


if __name__ == '__main__':
    main()
