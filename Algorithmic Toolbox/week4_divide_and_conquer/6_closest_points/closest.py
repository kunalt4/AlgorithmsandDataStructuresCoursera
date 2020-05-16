# Uses python3
import sys
from math import sqrt
from itertools import combinations


def min_dist(x, y):
    points = list(zip(x, y))
    points = sorted(points, key=lambda p: p[0])
    return sqrt(minimum_distance(points))


def minimum_distance(points):
    n = len(points)
    if n <= 3:
        return min_dist_brute_force_squared(points)
    mid = n//2
    min_left = minimum_distance(points[:mid])
    min_right = minimum_distance(points[mid:])
    min_lr = min(min_left, min_right)

    mid_points = [p for p in points if abs(points[mid][0] - p[0]) < min_lr]
    d = min_dist_brute_force_squared(mid_points, min_lr)
    return d


def min_dist_brute_force_squared(points, min_dist=10 ** 18):
    points = sorted(points, key=lambda p: p[1])
    for i in range(len(points)-1):
        p1 = points[i]
        for j in range(i+1, min(i+9, len(points))):
            p2 = points[j]
            cur_dist = (p1[0] - p2[0])**2 + (p1[1]-p2[1])**2

            if cur_dist < min_dist:
                min_dist = cur_dist
    return min_dist


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(min_dist(x, y)))
