import sys
n = int(sys.stdin.readline())
sys.setrecursionlimit(10**6) # 재귀 깊이 상한

graph = [[] for _ in range(n+1)]
parent = [0]*(n+1)
for _ in range(n-1) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
def find(start) :
    for i in graph[start] :
        if parent[i] == 0 :
            parent[i] = start
            find(i)
find(1)

for i in range(2, n+1) :
    print(parent[i])