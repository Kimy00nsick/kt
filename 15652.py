import sys
n, m = map(int, sys.stdin.readline().split())
s = [1]

def func() :
    if len(s) == m+1 :
        print(' '.join(map(str, s[1:])))
        return
    for i in range(1, n+1) :
        if i < max(s) :
            continue
        s.append(i)
        func()
        s.pop()
            
func()