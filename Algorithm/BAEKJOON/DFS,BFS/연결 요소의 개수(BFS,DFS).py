from collections import deque
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

list1 = [[] for i in range(n+1)]
visited_list1 = [0] * (n+1)
cnt = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    list1[u].append(v)
    list1[v].append(u)
"""
def bfs(i):
    que = deque([i])
    visited_list1[i] = 1
    
    while que:
        v = que.popleft()
        
        for node in list1[v]:
            if not visited_list1[node]:
                visited_list1[node] = 1
                que.append(node)

for i in range(1, n+1):
    if visited_list1[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)
"""
visited = []
def dfs(i):
    visited.append(i)
    
    for node in list1[i]:
        if node not in visited:
            dfs(node)

for i in range(1, n+1):
    if i not in visited:
        dfs(i)
        cnt += 1
        
print(cnt)   