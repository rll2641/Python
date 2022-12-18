'''
하나의 정점에서 다른 정점으로 바로 갈 수 있으면 최소 비용을, 갈 수 없다면
INF로 배열에 값을 저장합니다.
3중 for문을 통해 거쳐가는 정점을 설정한 후 해당 정점을 거쳐가서 비용이 줄어드는
경우에는 값을 바꿔줍니다.
위의 과정을 반복해 모든 정점 사이의 최단 경로를 탐색.
'''

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
v, e = map(int, input().split())

graph = [[INF] * (v + 1) for _ in range(v + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, v + 1):
    for b in range(1, v + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(e):
    # A에서 B로 가는 비용은 C라고 설정
    u, v, cost = map(int, input().split())
    graph[u][v] = cost

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 1->2 가는 최소비용
print(graph[1][2])