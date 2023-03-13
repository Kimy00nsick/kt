import sys
n, m = map(int, sys.stdin.readline().split())
s = []

def func() :
    if len(s) == m :
        print(' '.join(map(str, s)))
        return
    for i in range(1,n+1) :
        s.append(i)
        func()
        s.pop()
    
func()