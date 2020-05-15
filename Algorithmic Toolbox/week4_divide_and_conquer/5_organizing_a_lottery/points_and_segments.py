# Uses python3
import sys
import collections


def fast_count_segments(starts, ends, points):
    l_label = 1
    point_label = 2
    r_label = 3
    cnt = [0] * len(points)

    points_dict = collections.defaultdict(set)

    tuples = []

    for start in starts:
        tuples.append((start, l_label))

    for end in ends:
        tuples.append((end, r_label))

    for idx, point in enumerate(points):
        tuples.append((point, point_label))
        points_dict[point].add(idx)

    sort_vals = sorted(tuples, key=lambda p: (p[0], p[1]))

    overlap = 0
    for tup in sort_vals:
        if tup[1] == l_label:
            overlap += 1
        elif tup[1] == r_label:
            overlap -= 1
        else:
            indexes = points_dict[tup[0]]
            for i in indexes:
                cnt[i] = overlap

    # write your code here
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
