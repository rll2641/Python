# ------------------최단 거리-------------------- #
import heapq
import sys

station_dgraph = { # 지하철 노선도
    '용산': {'이촌': 2},
    '이촌': {'용산':2, '서빙고': 2, '동작': 3},
    '서빙고': {'이촌': 2, '한남': 2},
    '한남': {'서빙고':2 , '옥수': 2},
    '옥수': {'한남': 2, '압구정': 4},
    '흑석': {'동작': 1},
    '동작': {'흑석': 1, '구반포': 1, '총신대입구': 2, '이촌': 3},
    '구반포': {'동작': 1, '신반포': 1},
    '신반포': {'구반포':1, '고속터미널': 1},
    '고속터미널': {'신반포': 1, '잠원': 1, '교대': 2, '내방': 2},
    '압구정': {'옥수': 4, '신사': 2},
    '신사': {'압구정':2, '잠원': 1},
    '잠원': {'신사': 1, '고속터미널': 1},
    '총신대입구': {'동작': 2, '내방': 1, '사당': 1},
    '내방': {'총신대입구': 1, '고속터미널': 2},
    '사당': {'총신대입구': 1, '방배': 2},
    '방배': {'사당': 2, '서초': 2},
    '서초': {'방배':2, '교대': 1},
    '교대': {'서초': 1, '고속터미널': 2}
}

def dijkstra(start):

    distances = {node: sys.maxsize for node in station_dgraph}
    distances[start] = 0
    que = []
    
    heapq.heappush(que, (distances[start], start))
    
    while que:
        current_distance, node = heapq.heappop(que)
    
        if distances[node] < current_distance:
            continue
        
        for adjacency_node, distance in station_dgraph[node].items():
            weighted_distance = current_distance + distance
            
            if weighted_distance < distances[adjacency_node]:
                distances[adjacency_node] = weighted_distance
                heapq.heappush(que, (weighted_distance, adjacency_node))
    
    return distances