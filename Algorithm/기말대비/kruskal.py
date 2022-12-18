'''
무방향 그래프일 때, 최소비용 신장 트리 적용 가능
싸이클이 없는 연결된 무방향 그래프를 트리라고 부른다.
MST 문제의 답은 항상 트리가 된다.

크루스칼 알고리즘이란, 그래프 내의 모든 정점들을 가장 적은 비용으로 연결하기 위해
사용한다.

그래프 내의 모든 정점을 포함하고 사이클이 없는 연결 선을 그렷을 때, 가중치의
합이 최소가 되는 상황을 구하고 싶을 때 사용한다.

신장트리는 싸이클이 없기 때문에 정점의 갯수가 n개일 때, 간선이 n-1개가 된다.

각 단계에서 사이클을 이루지 않는 최소 비용 간선 선택
그래프의 간선들을 가중치의 오름차순으로 정렬
정렬된 간선 중에서 사이클을 형성하지 않는 간선을 현재 mst집합에 추가
만약 사이클을 형성하면 그 간선은 제외

사이클을 판단하기 위한 union-find 자료구조 사용
union-find란 서로소 집합을 표현하는 자료구조
서로 다른 두 집합을 병합하는 union연산, 집합 원소가 어떤 집합에 속해있는 지 찾는
find 연산을 지원하기에 이러한 이름을 붙임
https://chanhuiseok.github.io/posts/algo-33/
'''

# 노드의 개수와 간선의 개수 입력
v, e = map(int, input().split())
parent = [0] * (v + 1)

parent = [i for i in range(0, v + 1)]

kruskal_graph, save = [], []
minimum_cost = 0

# 간선 정보를 입력받아 cost를 기준으로 오름차순 정렬
for _ in range(e):
    u, v, cost = map(int, input().split())
    kruskal_graph.append((cost, u, v))

kruskal_graph.sort()

# 특정 원소가 속한 집합을 찾기
def find(parent, v):
    if parent[v] != v:
        parent[v] = find(parent, parent[v])
    return parent[v]

# 두 원소가 속한 집합을 합치기
def union(parent, u, v):
    u = find(parent, u)
    v = find(parent, v)
    if u < v:
        parent[v] = u
    else:
        parent[u] = v

# 정렬된 간선을 하나씩 확인
for edge in kruskal_graph:
    cost, u, v = edge
    # 두 노드의 루트 노드가 서로 다르다면 사이클이 발생하지 않은것이므로  
    if find(parent, u) != find(parent, v):
        # 신장 트리에 간선 추가
        union(parent, u, v)
        save.append([u, v, cost])
        minimum_cost += cost

print(save)
print(minimum_cost)