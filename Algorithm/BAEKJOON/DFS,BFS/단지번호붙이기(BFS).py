from collections import deque

def bfs(x, y):
    que = deque([(x, y)])
    # 단지를 찾고 실행했으니 +1
    global cnt_total_house
    cnt_total_house += 1
    
    house_map[x][y] = cnt_total_house
    
    cnt_num = 1
    
    while que:
        x, y = que.popleft()
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            if house_map[nx][ny] == 0:
                continue
            if house_map[nx][ny] == 1:
                que.append((nx, ny))
                house_map[nx][ny] = cnt_total_house
                cnt_num += 1
    return cnt_num

# 이중for문 탐색 중, 1을 만날 시 bfs시작.
# cnt_total_house = 1 첫 1 만나고 탐색 종료후 +1 ... 총 단지수는 cnt_total_house -= 1
# 미로찾기 알고리즘 이용

n = int(input())
house_map = []
for _ in range(n):
    house_map.append(list(map(int, input())))

cnt_total_house = 1
save_num = list()

for i in range(n):
    for j in range(n):
        if house_map[i][j] == 1:
            num = bfs(i, j)
            save_num.append(num)
            
save_num = sorted(save_num)

if cnt_total_house == 1:
    print(0)
else:
    print(cnt_total_house - 1)

if save_num:
    for i in save_num:
        print(i)
else:
    print(0)
    
""" (논리는 같으나 더 짧은 코드)
from collections import deque

def bfs(x, y):
    que = deque([(x, y)])
    house_map[x][y] = 0
    cnt = 1
    while que:
        x, y = que.popleft()
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if house_map[nx][ny] == 0:
                continue
            if house_map[nx][ny] == 1:
                que.append((nx, ny))
                house_map[nx][ny] = 0
                cnt += 1
    return cnt

n = int(input())
house_map = list()
cnt_total_house = list()

for _ in range(n):
    house_map.append(list(map(int, input())))
    
for i in range(n):
    for j in range(n):
        if house_map[i][j] == 1:
            cnt_total_house.append(bfs(i,j))

cnt_total_house.sort()
print(len(cnt_total_house))
for i in range(len(cnt_total_house)):
    print(cnt_total_house[i])
"""