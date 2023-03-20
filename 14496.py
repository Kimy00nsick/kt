import sys
from collections import deque
a ,b = map(int, sys.stdin.readline().split())
n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m) :
    start, end = map(int, sys.stdin.readline().split())
    if start == end :
        continue
    graph[start].append(end)
    graph[end].append(start)

def find(start, end) :
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue :
        x = queue.popleft()
        if x == end :
            return visited[x]-1
        for i in graph[x] :
            if visited[i] == 0 :
                queue.append(i)
                visited[i] = visited[x] + 1
    return -1


print(find(a, b))
