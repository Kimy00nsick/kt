import heapq
import sys
INF = int(1e9)

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, sys.stdin.readline().split())

start = x
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0 
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        
        for i in graph[now] :
            cost = dist + 1
            if cost < distance[i] :
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(start)
result = []
for i in range(1, n+1) :
    if distance[i] == k :
        result.append(i)

if len(result) != 0 :
    for i in result :
        print(i)
else :
    print(-1)
                
                