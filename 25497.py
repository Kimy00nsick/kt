import sys
from collections import deque

n = int(sys.stdin.readline())
skill = sys.stdin.readline().strip()
que = deque(skill)
arr = deque()
for i in range(n) :
    if que[0] == 'R' :
        if 'L' not in arr :
            break
        else :
            arr.append('R')
            arr.remove('L')
            que.popleft()
    elif que[0] == 'K' :
        if 'S' not in arr :
            break
        else :
            arr.append('K')
            arr.remove('S')
            que.popleft()
    else :
        arr.append(que.popleft())
    if len(que) == 0 : 
        break


print(len(arr)-arr.count('L')-arr.count('S'))



