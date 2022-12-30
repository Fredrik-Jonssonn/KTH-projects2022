# Fredrik Jonsson, grudat22 uppgift 4.2
import time
import matplotlib.pyplot as plt


def pow(n):
    """Return 2**n, where n is a nonnegative integer."""
    if n == 0:
        return 1
    x = pow(n // 2)
    if n % 2 == 0:
        return x * x
    return 2 * x * x


def sum1(a):
    """Return the sum of the elements in the list a."""
    n = len(a)
    if n == 0:
        return 0
    if n == 1:
        return a[0]
    return sum1(a[:n // 2]) + sum1(a[n // 2:])


def sum2(a):
    """Return the sum of the elements in the list a."""
    return _sum(a, 0, len(a) - 1)


def _sum(a, i, j):
    """Return the sum of the elements from a[i] to a[j]."""
    if i > j:
        return 0
    if i == j:
        return a[i]
    mid = (i + j) // 2
    return _sum(a, i, mid) + _sum(a, mid + 1, j)


def pow_benchmark(args):
    """Benchmark the pow function using the arguments contained in
    args and plot the result"""
    elapsed_time = []
    for n in args:
        start = time.time()
        pow(n)
        finish_time = time.time() - start
        elapsed_time.append(finish_time)
        print(n, finish_time)  # elapsed time
    plt.plot(args, elapsed_time, linestyle='--', marker='o')
    plt.xlabel('n')
    plt.ylabel('Elapsed time [s]')
    plt.title('pow benchmark')
    plt.show()


def sum1_benchmark(args):
    """Benchmark the sum1 function using the arguments contained in
    args and plot the result"""
    elapsed_time = []
    n = []
    for a in args:
        start = time.time()
        sum1(a)
        finish_time = time.time() - start
        elapsed_time.append(finish_time)
        print(len(a), finish_time)  # elapsed time
        n.append(len(a))
    plt.plot(n, elapsed_time, linestyle='--', marker='o')
    plt.xlabel('n')
    plt.ylabel('Elapsed time [s]')
    plt.title('sum1 benchmark')
    plt.show()


def sum2_benchmark(args):
    """Benchmark the sum2 function using the arguments contained in
    args and plot the result"""
    elapsed_time = []
    n = []
    for a in args:
        start = time.time()
        sum2(a)
        finish_time = time.time() - start
        elapsed_time.append(finish_time)
        print(len(a), finish_time)  # elapsed time
        n.append(len(a))
    plt.plot(n, elapsed_time, linestyle='--', marker='o')
    plt.xlabel('n')
    plt.ylabel('Elapsed time [s]')
    plt.title('sum2 benchmark')
    plt.show()


pow_benchmark([10, 100, 1_000, 10_000, 100_000, 500_000, 1_000_000, 1_100_000, 1_200_000, 1_300_000, 1_400_000 \
                  , 1_500_000, 1_600_000, 1_700_000, 1_800_000])
# sum1_benchmark([10 * [1], 100 * [1], 1_000 * [1], 10_000 * [1], 100_000 * [1], 500_000 * [1], 1_000_000 * [1], 1_100_000 * [1], \
#         1_200_000 * [1], 1_300_000 * [1], 1_400_000 * [1], 1_500_000 * [1], 1_600_000 * [1], 1_700_000 * [1], 1_800_000 * [1]])
# sum2_benchmark([10 * [1], 100 * [1], 1_000 * [1], 10_000 * [1], 100_000 * [1], 500_000 * [1], 1_000_000 * [1], 1_100_000 * [1], \
#         1_200_000 * [1], 1_300_000 * [1], 1_400_000 * [1], 1_500_000 * [1], 1_600_000 * [1], 1_700_000 * [1], 1_800_000 * [1]])