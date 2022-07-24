# bfs
from collections import deque

def bfs(x, y, cnt):
    que = deque([(x,y)])
    cnt += 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= len(island_map[0]) or island_map[nx][ny] == 0:
                continue
            if island_map[nx][ny] == 1:
                island_map[nx][ny] = 0
                que.append((nx, ny))
    return cnt
            
n, cnt = int(input()), 0
island_map = []

for _ in range(n):
    island_map.append(list(map(int, input())))

for i in range(n):
    for j in range(len(island_map[0])):
        if island_map[i][j] == 1:
            cnt = bfs(i, j, cnt)

print(cnt)