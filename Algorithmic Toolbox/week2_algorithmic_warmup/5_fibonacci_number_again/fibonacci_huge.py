# Uses python3
import sys


def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    fib_series = [0, 1]

    while True:
        fib_series.append((fib_series[-1]+fib_series[-2]) % m)
        if fib_series[-2:] == [0, 1]:
            break

    fib_series = fib_series[:-2]
    pisano = len(fib_series)
    n_new = n % pisano
    return fib_series[n_new] % m


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
