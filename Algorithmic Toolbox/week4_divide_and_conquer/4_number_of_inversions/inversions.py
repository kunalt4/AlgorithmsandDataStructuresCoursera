# Uses python3
import sys


def get_number_of_inversions(a):

    if len(a) == 1:
        return a, 0
    ave = len(a) // 2
    l, l_invert = get_number_of_inversions(a[:ave])
    r, r_invert = get_number_of_inversions(a[ave:])
    merged, merged_invert = merge(l, r)
    # write your code here
    return merged, merged_invert + l_invert + r_invert


def merge(lc, rc):
    number_of_inversions = 0
    res = []
    while lc and rc:
        if lc[0] <= rc[0]:
            res.append(lc.pop(0))
        else:
            res.append(rc.pop(0))
            number_of_inversions += len(lc)
    res += lc or rc
    return res, number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a)[1])
