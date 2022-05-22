import heapq
import sys

n = int(input())
heap = []
size = 0

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if size == 0:
            print(0)
        else:
            size -= 1
            print(heapq.heappop(heap)[1])
    else:
        size += 1
        # tuple에서 처음 절댓값 정렬후, 그다음 2번째원소 정렬
        heapq.heappush(heap, (abs(x), x))