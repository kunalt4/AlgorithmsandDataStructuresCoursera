# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [1,5,10]
    count = 0
    while m > 0:
        if m - coins[-1] >= 0:
            m = m-coins[-1]
            count+=1
        else:
            coins.pop()
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
