import sys

n = int(sys.stdin.readline())

def func(n, a, b) :
    if n == 1 :
        print(a)
        return
    
    func(n-1, a*b, b+1)

if n > 0 :
    func(n, 1, 2)
else :
    print(1)