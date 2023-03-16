import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 상한
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start) :
    visited[start] = True
    for i in graph[start] :
        if visited[i] == False :
            visited[i] = True
            dfs(i)
result = 0
for i in range(1,n+1) :
    if visited[i] == False :
        dfs(i)
        result += 1


print(result)