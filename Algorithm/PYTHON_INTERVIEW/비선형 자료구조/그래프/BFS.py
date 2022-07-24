from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

def bfs(v):
    visited, que = [v], deque([v])    
    while que:
        v = que.popleft()
        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                que.append(i)
    return visited

print(bfs(1))