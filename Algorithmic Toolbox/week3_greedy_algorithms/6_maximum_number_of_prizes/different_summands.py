# Uses python3
import sys

def optimal_summands(n):
    summands = []
    start = 1
    end = n
    
    while end != 0:
        if start < end/2:
            summands.append(start)
            end -= start
        else:
            summands.append(end)
            end = 0
        start += 1
        
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
