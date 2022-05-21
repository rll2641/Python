from collections import deque

n, k = map(int, input().split())

que = deque([i for i in range(1, n+1)])

print("<", end="")
while que:
    for _ in range(k-1):
        que.append(que[0])
        que.popleft()
    i = que.popleft()
    if not que:
        print(f"{i}>")
    else:
        print(f"{i}, ", end="")