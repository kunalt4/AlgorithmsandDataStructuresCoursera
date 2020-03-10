# # Uses python3
import sys

def get_majority_element(a):
    
    if len(a) == 0:
        return None
    if len(a) == 1:
        return a[0]
    
    half = len(a)//2
    left = get_majority_element(a[0:half])
    right = get_majority_element(a[half:])

    if left == right:
        return left
    if a.count(left) > half:
        return left
    if a.count(right) > half:
        return right

    return None
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a):
        print(1)
    else:
        print(0)
