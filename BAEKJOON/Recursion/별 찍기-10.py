def star(i, j):
    while i != 0:
        if i%3 == 1 and j%3 == 1:
            print(" ", end="")
            return
        i //= 3
        j //= 3
    print("*", end="")

n = int(input())

for i in range(n):
    for j in range(n):
        star(i, j)
    print("")