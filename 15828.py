import sys
from collections import deque
n = int(sys.stdin.readline())
a = deque()
while True :
    num = int(sys.stdin.readline())
    a.append(num)
    if num == -1 :
        a.pop()
        break
b = deque()
while True :
    if len(b) != n :
        if a[0] != 0 :
            b.append(a.popleft())
        elif a[0] == 0 and len(b) != 0:
            a.popleft()
            b.popleft()
        if len(a) == 0 :
            break
    elif len(b) == n :
        if a[0] !=0 :
            a.popleft()
        elif a[0] == 0 and len(b) != 0 :
            a.popleft()
            b.popleft()
        if len(a) == 0 :
            break

        
if len(b) == 0 :
    print('empty')
else :            
    print(' '.join(map(str, list(b))))

