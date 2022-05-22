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
            print(heapq.heappop(heap))
    else:
        size += 1
        heapq.heappush(heap, x)
            