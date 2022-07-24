times = [[3,1,5], [3,2,2], [2,1,2], [3,4,1], [4,5,1], [5,6,1], [6,7,1], [7,8,1], [8,1,1]] # 출발지, 도착지, 소요시간

from collections import defaultdict
import heapq

graph = defaultdict(list)
dist = defaultdict(int)
n, k = 8, 3
q = [(0, k)] # (소요시간, 정점)

for u, v, w in times:
    graph[u].append((v,w)) # 도착지 소요시간

while q:
    time, node = heapq.heappop(q)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]:
            alt = time + w
            heapq.heappush(q, (alt, v)) # 소요시간, 정점

if len(dist) == n:
    print(max(dist.values()))
else:
    print('-1')