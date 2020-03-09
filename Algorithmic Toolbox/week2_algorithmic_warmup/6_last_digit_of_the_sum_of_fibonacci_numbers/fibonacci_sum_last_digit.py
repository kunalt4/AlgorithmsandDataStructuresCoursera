# Uses python3
import sys


def fibonacci_sum_naive(n):

    n += 2

    fib_series = [0, 1]

    while True:
        fib_series.append((fib_series[-1]+fib_series[-2]) % 10)
        if fib_series[-2:] == [0, 1]:
            break

    fib_series = fib_series[:-2]
    pisano = len(fib_series)
    n_new = n % pisano
    return (fib_series[n_new] - 1) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
