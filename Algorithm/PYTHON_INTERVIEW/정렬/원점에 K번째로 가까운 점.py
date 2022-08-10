# 평면상에 points 목록이 있을 때, 원점(0,0)에서 K번 가까운 점 목록을 순서대로 출력하라.
# 평면상 두 점의 거리는 유클리드 거리로 한다.
import heapq
import math

points, K = [[1,3], [-2, 2]], 1

def KCloset(points: list[list[int]], k: int):
    heap = []
    for (x, y) in points:
        dist = math.sqrt((0-x)**2 + (0-y)**2)
        heapq.heappush(heap, (dist, x, y))
    
    result = []
    
    for _ in range(k):
        (dist, x, y) = heapq.heappop(heap)
        result.append((x,y))
    
    return result

print(KCloset(points, K))