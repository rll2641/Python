n = int(input())
fat_list = []
for _ in range(n):
    x, y = map(int, input().split())
    fat_list.append((x,y))

for i in fat_list:
    rank = 1
    
    for j in fat_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")