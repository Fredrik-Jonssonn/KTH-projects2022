# Fredrik Jonsson, grudat22 uppgift 4.2

def counting_sort(v):
    """Sort the elements of the vector v in ascending order,
    v stores non-negative integers"""
    k = max(v)
    count = [0 for _ in range(k + 1)]
    output = [0 for _ in range(len(v))]
    for element in v:
        count[element] += 1
    for i in range(1, k + 1):
        count[i] += count[i - 1]
    for i in range(len(v)):
        output[count[v[i]] - 1] = v[i]
        count[v[i]] -= 1
    for i in range(len(v)):
        v[i] = output[i]


# Unit Test
def main():
    test1 = [1]
    counting_sort(test1)
    assert test1 == [1]
    test2 = [0, 2, 6, 0, 0, 2, 3, 4, 4]
    counting_sort(test2)
    assert test2 == [0, 0, 0, 2, 2, 3, 4, 4, 6]
    test3 = [7, 5, 4, 3, 2, 6, 1]
    counting_sort(test3)
    assert test3 == [1, 2, 3, 4, 5, 6, 7]
    test4 = [1, 6, 1, 3, 1, 1, 7, 1]
    counting_sort(test4)
    assert test4 == [1, 1, 1, 1, 1, 3, 6, 7]
    test5 = [1000, 593, 10000, 3, 1, 1, 7, 1]
    counting_sort(test5)
    assert test5 == [1, 1, 1, 3, 7, 593, 1000, 10000]


if __name__ == '__main__':
    main()
