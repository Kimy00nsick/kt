import sys
from collections import deque

t = int(sys.stdin.readline())
result_arr = []
def func() : 
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0]*n for _ in range(m)]
    for _ in range(k) :
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0
    def bfs(x, y) :
        queue = deque()
        queue.append((x, y))
        graph[x][y] = 0
        while queue :
            x, y = queue.popleft()
            for i in range(4) :
                nx, ny = x+dx[i], y+dy[i]
                if nx < 0 or nx >= m or ny < 0 or ny >= n :
                    continue
                if graph[nx][ny] == 1 :
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
        return 1

    for i in range(n) :
        for j in range(m) :
            if graph[j][i] == 1 :
                result += bfs(j, i)
            elif graph[j][i] == 0 :
                continue       
    result_arr.append(result)
    
for i in range(t) :
    func()
for i in range(t) :
    print(result_arr[i])