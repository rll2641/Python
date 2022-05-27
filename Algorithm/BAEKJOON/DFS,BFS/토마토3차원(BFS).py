from collections import deque
import sys

m, n, h = map(int, input().split())
box, que = [], deque([])
max_value = -1

for i in range(h):
    save = []
    for j in range(n):
        save.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if save[j][k] == 1:
                que.append((i,j,k))
    box.append(save)
    
dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

while que:
    z, x, y = que.popleft()
        
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
            
        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and box[nz][nx][ny] == 0:
                que.append((nz,nx,ny))
                box[nz][nx][ny] = box[z][x][y] + 1

for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        max_value = max(max_value, max(j))
print(max_value - 1)