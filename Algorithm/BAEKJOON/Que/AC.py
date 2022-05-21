from collections import deque
import sys

t = int(input())

for _ in range(t):
    order = list(input())
    n = int(input())
    matrix = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    r = True # true, 일반 배열, false, 뒤집힌 배열
    error = True
    
    for i in order:
        if i == 'R':
            if r:
                r = False
            else:
                r = True
        if i == 'D':
            if len(matrix) - 1:
                if r:
                    matrix.popleft()
                else:
                    matrix.pop()
            else:
                error = False
                break
    
    if not error:
        print('error')
        continue
    elif n == 0:
        print('[]')
        continue
    
    if r:
        print("[" + ",".join(matrix) + "]")
    else:
        matrix.reverse()
        print("[" + ",".join(matrix) + "]")