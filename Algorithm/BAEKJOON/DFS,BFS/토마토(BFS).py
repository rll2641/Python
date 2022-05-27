from collections import deque

# 미로 알고리즘 응용
m, n = map(int, input().split())
box, que = list(), deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(n):
    box.append(list(map(int, input().split())))
    for j in range(m):
        if box[i][j] == 1:
            que.append((i,j))

def bfs():
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if box[nx][ny] == 0:
                que.append((nx, ny))
                box[nx][ny] = box[x][y] + 1

bfs()
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit(0)
max_value = max(map(max, box))
print(max_value - 1)