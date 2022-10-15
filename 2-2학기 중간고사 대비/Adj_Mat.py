n, e = map(int, input().split())
adj_mat = [[0] * n for _ in range(n)]

for _ in range(e):
    v1, v2 = map(int, input().split())
    adj_mat[v1][v2] = 1
    adj_mat[v2][v1] = 1

print(adj_mat)