import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited_dfs , visited_bfs = [0]*(n+1), [0]*(n+1)

for i in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1][v2] = graph[v2][v1] = 1
    
def dfs(start_node):
    visited_dfs[start_node] = 1
    print(start_node, end=" ")
    
    for i in range(1, n+1):
        if graph[start_node][i] == 1 and visited_dfs[i] == 0:
            dfs(i)

def bfs(start_node):
    que = deque([start_node])
    visited_bfs[start_node] = 1
    
    while que:
        v = que.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited_bfs[i] == 0:
                que.append(i)
                visited_bfs[i] = 1
                
dfs(v)
print()
bfs(v)