import sys
from collections import deque
n ,m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m) :
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

def find(start) :
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue :
        x = queue.popleft()
        for i in graph[x] :
            if visited[i] == 0 :
                queue.append(i)
                visited[i] = visited[x] + 1

find(1)
print(visited.index(max(visited)), max(visited)-1, visited.count(max(visited)))
