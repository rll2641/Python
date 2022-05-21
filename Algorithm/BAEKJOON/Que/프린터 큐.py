t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    impor = list(map(int, input().split()))
    save = [0 for i in range(n)]
    save[m] = 1
    cnt = 0
    while True:
        if impor[0] == max(impor):
            cnt += 1
            if save[0] == 1:
                print(cnt)
                break
            else:
                del impor[0]
                del save[0]
        else:
            impor.append(impor[0])
            del impor[0]
            save.append(save[0])
            del save[0]