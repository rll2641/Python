n = int(input())
is_true, result = False, 0

for i in range(1, n+1):
    num_list = list(map(int, str(i)))
    if (i + sum(num_list)) == n:
        is_true, result = True, i
        break

if is_true:
    print(result)
else:
    print(0)