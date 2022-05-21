stack = []
save = []
count = 1
result = True

n = int(input())

for _ in range(n):
    num = int(input())
    
    while count <= num:
        stack.append(count)
        save.append('+')
        count += 1
    
    if stack[-1] == num:
        stack.pop()
        save.append('-')
    else:
        result = False
    
if result:
    for i in save:
        print(i)
else:
    print('NO')