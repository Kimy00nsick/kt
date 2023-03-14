import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
# graph = []
# visited = [1]
# for i in range(m) :
#     graph.append(list(map(int, sys.stdin.readline().split())))

# def bfs() :
#     for i in range(m) :
#         for j in range(2) :
#             if graph[i][j] in visited :
#                 visited.append(graph[i][0])
#                 visited.append(graph[i][1])

# bfs()

# visited = set(visited)
# print(len(visited)-1)
graph = [[]*n for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)

def dfs(start) :
    visited[start] = 1
    for i in graph[start] :
        if visited[i] == 0 :
            dfs(i)
dfs(1)            
print(sum(visited)-1)
            