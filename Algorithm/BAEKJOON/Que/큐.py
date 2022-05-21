import sys
from collections import deque

que = deque()
que_size = 0
n = int(input())

for _ in range(n):
    option = sys.stdin.readline().split()
    if option[0] == "push":
        que.append(option[1])
        que_size += 1
        
    elif option[0] == "pop":
        if que:
            print(que.popleft())
            que_size -= 1
        else:
            print(-1)
    elif option[0] == "size":
        print(que_size)
    elif option[0] == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif option[0] == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif option[0] == "back":
        if que:
            print(que[-1])
        else:
            print(-1)