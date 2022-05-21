from collections import deque
n = int(input())

que = deque([i for i in range(1, n+1)])

while len(que) > 1:
    que.popleft()
    save = que.popleft()
    que.append(save)
    
print(que[0])