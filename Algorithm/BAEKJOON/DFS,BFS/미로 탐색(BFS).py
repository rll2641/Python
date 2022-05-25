import sys
from collections import deque

maze = list()
n, m = map(int, sys.stdin.readline().split())

for _ in range(n):
    maze.append(list(map(int, input())))

# 미로 탐색은 인접 노드를 탐색하는 bfs가 적합
# 0,0에서 시작, 네 방향 조건 검사
# 이동 및 이동마다 숫자 증가
def bfs(x, y):
    que = deque([(x, y)])
    
    while que:
        x, y = que.popleft()
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                que.append((nx, ny))
    print(maze[n-1][m-1])

bfs(0,0)