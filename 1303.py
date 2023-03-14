# import sys
# n, m = map(int, sys.stdin.readline().split())

# graph = []
# for i in range(m) :
#     graph.append(list(map(str, sys.stdin.readline().strip())))
    
# visited = []
            
# def dfs(x, y) :
#     if x <= -1 or x >= n or y <= -1 or y >= m :
#         return False
    
#     if graph[x][y] == 'W' :
#         graph[x][y] == 1
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False

# for i in range(n) :
#     for j in range(m) :
#         if dfs(i, j) == True :
#             visited.append([i,j])

# print(visited)
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = [] 
result = [0, 0] # 결과 저장
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(m) :
    graph.append(list(sys.stdin.readline()))

def bfs(x, y, wb) :
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 1
    count = 1
    while queue:
        x, y = queue.popleft()    
        for i in range(4) :
            nx, ny = dx[i]+x, dy[i]+y
            if nx < 0 or nx >= m or ny < 0 or ny >= n :
                continue
            if graph[nx][ny] == wb :    
                graph[nx][ny] = 1
                queue.append((nx, ny))
                count += 1
    return count**2
         

for i in range(m) :
    for j in range(n) :
        if graph[i][j] == 'W' :
            result[0] += (bfs(i, j, 'W'))
        if graph[i][j] == 'B' :
            result[1] += (bfs(i, j, 'B'))
            
print(' '.join(map(str, result)))