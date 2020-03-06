# Uses python3
import sys


def fibonacci_sum_naive(m):

    m = m + 2

    fib_series = [0, 1]

    for i in range(2, 60):
        fib_series.append((fib_series[-1]+fib_series[-2]))

    m = m % 60

    return fib_series[m] - 1


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    num = ((fibonacci_sum_naive(to) -
            (fibonacci_sum_naive(from_ - 1))) % 10+10) % 10
    print(num)
