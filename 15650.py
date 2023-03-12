import sys

n, m = map(int, sys.stdin.readline().split())
s = []
def a(count) :
    if len(s) == m :
        print(' '.join(map(str, s)))
        return
    
    for i in range(count, n+1) :
        if i not in s :
            s.append(i)
            a(i+1)
            s.pop()

a(1)