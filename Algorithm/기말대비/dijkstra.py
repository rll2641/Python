from collections import defaultdict
import heapq
import sys

v, e = map(int, input().split())

dijsktra_graph = defaultdict(dict)

for _ in range(e):
    u, v, cost = map(int, input().split())
    dijsktra_graph[u].update({v:cost})
    dijsktra_graph[v].update({u:cost})
    
def dijsktra(start, end):
    distance = {n: sys.maxsize for n in dijsktra_graph}
    distance[start] = 0
    que= []
    heapq.heappush(que, (distance[start], start))
    
    while que:
        dist, node = heapq.heappop(que)
        
        if distance[node] < dist:
            continue
        
        for n, d in dijsktra_graph[node].items():
            min_distance = dist + d
            
            if min_distance < distance[n]:
                distance[n] = min_distance
                heapq.heappush(que, (min_distance, n))
    
    return distance.get(end)

print(dijsktra(1, 4))