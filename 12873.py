import sys
from collections import deque
n = int(sys.stdin.readline())

a = deque()

for i in range(n) :
    a.append(i+1)


a.popleft() 
for i in range(1,n-1) :
    t = ((i+1)**3)%len(a)
    for i in range(t-1) :
        a.append(a.popleft())
    a.popleft()

if n == 1 :
    print(1)
elif n ==2 :
    print(2)
elif n == 3 :
    print(2)
else :
    print(a[0])