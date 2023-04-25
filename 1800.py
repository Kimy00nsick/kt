import sys
import heapq

n, p, k = map(int, sys.stdin.readline().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(p) :
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0 
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)

if distance[-1] == INF :
    print(-1) 
else :
    print(distance)          
    
