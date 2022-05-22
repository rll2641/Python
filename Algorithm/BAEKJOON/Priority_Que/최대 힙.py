import sys
import heapq

n = int(input())

heap = []
size = 0
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if size == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
            size -= 1
    else:
        size += 1
        heapq.heappush(heap, (-x, x))
        
    """
    2번째 방법
import sys
class Max_heap:
    def __init__(self):
        self.heap = [None]
        self.heap_size = 0
    def insert_node(self, key):
        self.heap.append(key)
        self.heap_size += 1
        idx = self.heap_size
        
        while idx != 1 and key > self.heap[idx//2]:
            self.heap[idx] = self.heap[idx//2]
            idx //= 2
        self.heap[idx] = key
    def delete_node(self):
        p, c = 1, 2
        item = self.heap[p]
        temp = self.heap[self.heap_size]
        self.heap_size -= 1
        
        while c <= self.heap_size:
            if c < self.heap_size and self.heap[c] < self.heap[c + 1]:
                c += 1
            if temp > self.heap[c]:
                break
            self.heap[p] = self.heap[c]
            p = c
            c *= 2

        self.heap[p] = temp
        self.heap.pop()
        return item

n = int(input())
heap = Max_heap()

for _ in range(n):
    x = int(sys.stdin.readline())
    
    if x == 0:
        if heap.heap_size == 0:
            print(0)
        else:
            print(heap.delete_node())
    else:
        heap.insert_node(x)
    
    """