# ------------------최단 거리-------------------- #
import heapq
import sys

station_dgraph = { # 지하철 노선도
    '용산': {'이촌': 1.9},
    '이촌': {'용산': 1.9, '서빙고': 1.7, '동작': 2.7},
    '서빙고': {'이촌': 1.7, '한남': 1.9},
    '한남': {'서빙고': 1.9 , '옥수': 1.6},
    '옥수': {'한남': 1.6, '압구정': 2.1},
    '흑석': {'동작': 1.4},
    '동작': {'흑석': 1.4, '구반포': 1.0, '총신대입구': 1.8, '이촌': 2.7},
    '구반포': {'동작': 1.0, '신반포': 1.0},
    '신반포': {'구반포': 1.0, '고속터미널': 1.0},
    '고속터미널': {'신반포': 1.0, '잠원': 1.2, '교대': 1.6, '내방': 2.2},
    '압구정': {'옥수': 2.1, '신사': 1.5},
    '신사': {'압구정': 1.5, '잠원': 1.0},
    '잠원': {'신사': 1.0, '고속터미널': 1.2},
    '총신대입구': {'동작': 1.8, '내방': 1.0, '사당': 1.1},
    '내방': {'총신대입구': 1.0, '고속터미널': 2.2},
    '사당': {'총신대입구': 1.1, '방배': 1.6},
    '방배': {'사당': 1.6, '서초': 1.7},
    '서초': {'방배': 1.7, '교대': 1.0},
    '교대': {'서초': 1.0, '고속터미널': 1.6}
}

def dijkstra(start):

    station_distance = {node: sys.maxsize for node in station_dgraph}
    station_distance[start] = 0
    que = []
    heapq.heappush(que, (station_distance[start], start))

    while que:
      distance, node = heapq.heappop(que)
      
      if station_distance[node] < distance:
            continue
          
      for n, d in station_dgraph[node].items():
        min_distance = distance + d
        
        if min_distance < station_distance[n]:
          station_distance[n] = min_distance
          heapq.heappush(que,(min_distance, n))

    return station_distance