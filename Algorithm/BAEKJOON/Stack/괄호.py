t = int(input())

for _ in range(t):
    ps = list(input())
    count = 0
    
    for i in ps:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            print('NO')
            break
        
    if count > 0:
        print('NO')
    elif count == 0:
        print('YES')