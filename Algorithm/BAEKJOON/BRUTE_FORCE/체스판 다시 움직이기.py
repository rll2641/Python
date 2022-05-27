n, m = map(int, input().split())
ches,min_ = [], []
for _ in range(n):
    ches.append(list(map(str, input())))

for a in range(n - 7):
    for i in range(m - 7):
        idx1 = 0
        idx2 = 0
        for b in range(a, a + 8):
            for j in range(i, i + 8):              # 8X8 범위를 B와 W로 번갈아가면서 검사
                if (j + b)%2 == 0:
                    if ches[b][j] != 'W': idx1 += 1  
                    if ches[b][j] != 'B': idx2 += 1
                else :
                    if ches[b][j] != 'B': idx1 += 1
                    if ches[b][j] != 'W': idx2 += 1
        min_.append(idx1)                          # W로 시작했을 때 칠해야 할 부분
        min_.append(idx2)   

print(min(min_))