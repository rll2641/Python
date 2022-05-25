from collections import deque

n = int(input()) # 노드 수
e = int(input()) # 간선 수

network = [[] for _ in range(n+1)]
visited_bfs = [0] * (n + 1)
visited_dfs = [0] * (n + 1)

for _ in range(e):
    v1, v2 = map(int, input().split()) # 정점1,2
    network[v1].append(v2)
    network[v2].append(v1)

def bfs(start_node):
    que = deque([start_node])
    visited_bfs[start_node] = 1
    cnt = 0
    
    while que:
        v = que.popleft()
        for i in network[v]:
            if visited_bfs[i] == 0:
                que.append(i)
                visited_bfs[i] = 1
                cnt += 1
    return cnt

cnt = 0

def dfs(start_node):
    visited_dfs[start_node] = 1
    global cnt
    for node in network[start_node]:
        if visited_dfs[node] == 0:
            cnt += 1
            dfs(node)

dfs(1)
print(cnt)
