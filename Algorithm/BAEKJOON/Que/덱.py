from collections import deque
import sys

n = int(input())

d = deque()

for _ in range(n):
    option = sys.stdin.readline().split()
    if option[0] == "push_front":
        d.appendleft(option[1])
    elif option[0] == "push_back":
        d.append(option[1])
    elif option[0] == "pop_front":
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif option[0] == "pop_back":
        if d:
            print(d.pop())
        else:
            print(-1)
    elif option[0] == "size":
        print(len(d))
    elif option[0] == "empty":
        if d:
            print(0)
        else:
            print(1)
    elif option[0] == "front":
        if d:
            print(d[0])
        else:
            print(-1)
    elif option[0] == "back":
        if d:
            print(d[-1])
        else:
            print(-1)