# dfs

# 재귀    
def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= len(island_map[0]) or island_map[x][y] != 1:
        return 
    
    island_map[x][y] = 0
    
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)
    
n, cnt = int(input()), 0
island_map = []

for _ in range(n):
    island_map.append(list(map(int, input())))

for i in range(n):
    for j in range(len(island_map[0])):
        if island_map[i][j] == 1:
            dfs(i, j)
            cnt += 1
print(cnt)