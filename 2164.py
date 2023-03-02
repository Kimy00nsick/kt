import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()

for i in range(n) :
    queue.append(i+1)

while True :
    queue.popleft()
    queue.append(queue.popleft())
    if len(queue) == 1 :
        break

print(queue[0])
