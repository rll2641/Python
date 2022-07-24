from collections import defaultdict
import heapq as hq

edges = [[0,1,100], [1,2,100], [0,2,500]]
src, dst, k, n = 0, 2, 0, 3

def findCheapestPrice(n, flights, src, dst, K):
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v,w))
    
    Q = [(0, src, K)] # 가격, 정점, 경유횟수
    
    while Q:
        price, node, k = hq.heappop(Q)
        if node == dst:
            return price
        if K >= 0:
            for v, w in graph[node]:
                alt = price + w
                hq.heappush(Q, (alt, v, k - 1))
    return -1


        