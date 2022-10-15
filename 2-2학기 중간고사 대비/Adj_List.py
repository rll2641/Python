n, e = map(int, input().split())

adj_lst = [[] for _ in range(n)]

print(adj_lst)
for _ in range(e):
    v1, v2 = map(int, input().split())
    adj_lst[v1].append(v2)
    adj_lst[v2].append(v1)
    
print(adj_lst)