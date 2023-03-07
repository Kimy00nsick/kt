import sys
from collections import deque
n = int(sys.stdin.readline())

a = deque()

for i in range(n) :
    a.append(i+1)


for i in range(1,n+1) :
    t = (i**3%len(a))-1
    a.rotate(-t)
    a.popleft()
    if len(a) == 1:
        break


if n == 1 :
    print(1)    
else :
    print(a[0])