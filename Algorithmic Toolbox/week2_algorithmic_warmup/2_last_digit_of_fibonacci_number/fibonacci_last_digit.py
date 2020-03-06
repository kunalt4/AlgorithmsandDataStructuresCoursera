# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
        return 1

    fib_list = []

    fib_list.append(0)
    fib_list.append(1)

    for i in range(2, n+1):
        fib_list.append((fib_list[i-1] + fib_list[i-2]) % 10)

    return fib_list[-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
