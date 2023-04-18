import sys
import heapq
INF = int(1e9)
# v 정점의 개수, e 간선의 개수, p 건우의 위치
v, e, p = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)

for i in range(e) :
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

gun = distance[p]   # 출발점에서 건우까지 거리
end = distance[-1]  # 출발점에서 목적지까지 거리

distance = [INF]*(v+1)  # 초기화
dijkstra(p)
guntoend = distance[-1] # 건우에서 목적지까지 거리    

if gun + guntoend == end :
    print('SAVE HIM')
else :
    print('GOOD BYE')