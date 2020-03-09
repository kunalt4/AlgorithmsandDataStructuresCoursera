# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    n = n % 60
    fib_series = [0, 1]

    for i in range(2, n+2):
        fib_series.append((fib_series[-1]+fib_series[-2]))

    return (fib_series[n]*fib_series[n+1]) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
