#Uses python3

import sys

def largest_number(a):
    def isGreaterOrEqual(d,e):
        return int(str(d)+str(e)) >= int(str(e)+str(d))

    res = ""
    while a:
        maxDigit = a[0]
        for digit in a:
            if isGreaterOrEqual(digit,maxDigit):
                maxDigit = digit
        res+=str(maxDigit)
        a.remove(maxDigit)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
