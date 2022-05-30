n = int(input())
result = 0
while True:
    if n == 1:
        break
    elif n % 3 == 0:
        n = n/3
        result += 1
        continue
    elif n % 2 == 0:
        n = n/2
        result += 1
        continue
    else:
        n -= 1
        result += 1

print(result)