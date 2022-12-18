'''
시작 정점에서부터 출발하여 신장 트리 집합을 단계적으로 확장해 나감
신장 트리 집합에 인접한 정점 중에서 최저 간선으로 연결된 정점 선택하여
신장 트리 집합에 추가함
이 과정은 간선의 개수가 n-1개의 개수를 가질 때까지 반복
'''

from collections import defaultdict
import heapq


v, e = map(int, input().split())
prim_graph, visited = defaultdict(list), [0] * (v+1)

for _ in range(e):
    u, v, cost = map(int, input().split())
    prim_graph[u].append([cost, u, v])
    prim_graph[v].append([cost, v, u])

def prim(start):
    save, minimum_cost = [], 0
    visited[start] = 1
    edges = prim_graph[start]
    heapq.heapify(edges)
    
    while edges:
        cost, u, v = heapq.heappop(edges)
        
        if visited[v] == 0:
            visited[v] = 1
            save.append([u, v, cost])
            minimum_cost += cost
            
            for e in prim_graph[v]:
                if visited[e[2]] == 0:
                    heapq.heappush(edges, e)
    
    print(save)                
    return minimum_cost

print(prim(1))