# python3
import sys


def compute_min_refills(distance, tank, stops):
    start = 0
    end = distance
    stops.insert(0,start)
    stops.append(end)
    count = 0
    diff_vals = []
    for i in range(len(stops)-1):
        if (stops[i+1]-stops[i])>tank:
            return -1
    cur_distance = 0
    while cur_distance + tank < end:
        cur_distance += tank
        i = next(x[0] for x in enumerate(stops) if x[1] > cur_distance)
        count+=1
        cur_distance = stops[i-1]
        # print(cur_distance)
    return count

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
