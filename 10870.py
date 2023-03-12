import sys

n = int(sys.stdin.readline())
a = 0
b = 1
def func(n, a, b) : 
    if n == 1 :
        print(b)
        return
    
    func(n-1, b, a+b)

if n > 1 :
    func(n, a, b)
elif n == 1 :
    print(1)
else :
    print(0)