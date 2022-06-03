import sys

input = sys.stdin.readline # 빠른 입력
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 방문 체크
visited = [False]*(n+1)
# 최단거리 테이블
distance = [INF]*(n+1)

# 노드 연결정보
graph = [[] for i in range(n+1)]

for _ in range(m):
  # a번노드에서 b번 노드로 가는 비용c
  a,b,c = map(int, input().split())
  graph[a].append((b,c))

# 방문하지 않은 노드 중 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

# 다익스트라 알고리즘
def dijkstra(start):
  # 시작 노드
  distance[start] = 0
  visited[start] = True
  # 출발노드와 인접노드에 대해 최단거리 테이블 갱신
  for j in graph[start]:
    distance[j[0]] = j[1]

  # 모든 노드에 대해 반복
  for i in range(n-1):
    # 현재 최단거리가 가장 짧은 노드를 꺼내서 방문처리
    now = get_smallest_node()
    visited[now] = True
    # 선택된 노드와 연결된 다른 노드를 확인
    for j in graph[now]:
      # 선택된 노드를 통해 가는 비용을 다시 계산
      # 선택된 노드의 비용 + 연결된 노드로 가는 비용
      cost = distance[now] + j[1]
      # 선택된 노드를 거쳐서 가는 비용이 더 짧은 경우
      if cost<distance[j[0]]:
        distance[j[0]] = cost # 최단거리 테이블 갱신
  
#다익스트라 알고리즘수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
  # 도달할 수 없는 경우
  if distance[i] == INF:
    print("infinity")
  else:
    print(distance[i])