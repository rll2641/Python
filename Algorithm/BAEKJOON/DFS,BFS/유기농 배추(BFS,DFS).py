import sys
from collections import deque
sys.setrecursionlimit(10000)

def bfs(x, y): 
    que = deque([(x, y)])
    farm[x][y] = 0
    global cnt
    cnt += 1
    while que:
        x, y = que.popleft()
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <= 0 or ny <= 0 or nx > n or ny > m:
                continue
            if farm[nx][ny] == 0:
                continue
            if farm[nx][ny] == 1:
                que.append((nx, ny))
                farm[nx][ny] = 0
                
def dfs(x, y):
    farm[x][y] = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0<= nx < n) and (0<= ny < m):
            if farm[nx][ny] == 1:
                farm[nx][ny] = 0
                dfs(nx,ny)
    
t = int(input())

for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    farm = [[0]*m for _ in range(n)] 
    
    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)