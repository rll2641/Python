from collections import deque

n, k = map(int, input().split())
list1 = [0] * (10 ** 5 + 1)

def bfs():
    que = deque([n])
    
    while que:
        x = que.popleft()
        dx = [x-1, x+1, x*2]
        
        if x == k:
            print(list1[x])
            break
        
        for nx in dx:
            if 0 <= nx <= 10**5 and list1[nx] == 0:
                list1[nx] = list1[x] + 1
                que.append(nx)

bfs()