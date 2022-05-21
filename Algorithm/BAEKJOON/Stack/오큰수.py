import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

stack = []
save_value = [-1]*n

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        save_value[stack.pop()] = a[i]
        
    stack.append(i)

print(*save_value)