import heapq as hq
import sys

min_heap, max_heap = [], []
min_size, max_size = 0, 0
n = int(input())
# 두 힙의 사이즈가 같을 때, 최대힙부터 넣어주어야 한다.
# 중간값은 항상 최대힙의 첫 요소가 된다.
# 만약 최대 힙의 첫 요소 * -1가 최소 힙의 첫 요소보다 크면 둘이 바꿔주어야 한다.
for _ in range(n):
    num = int(sys.stdin.readline())
    
    if max_size == min_size:
        hq.heappush(max_heap, -num)
        max_size += 1
    else:
        hq.heappush(min_heap, num)
        min_size += 1
    
    if max_size >= 1 and min_size >= 1 and max_heap[0] * -1 > min_heap[0]:
        save_max = hq.heappop(max_heap) * -1
        save_min = hq.heappop(min_heap)
        hq.heappush(max_heap, save_min * -1)
        hq.heappush(min_heap, save_max)

    print(max_heap[0] * -1)