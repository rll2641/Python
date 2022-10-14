from heapq import heapify


class Min_Heap:
    def __init__(self):
        self.heap = [None]
        self.heap_size = 0 
    
    def insert_min_heap(self, key):
        self.heap.append(key)
        self.heap_size += 1
        
        index = self.heap_size
        
        while index != 1 and key < self.heap[index//2]:
            self.heap[index] = self.heap[index//2]
            index //= 2
        self.heap[index] = key
        
    def removed_key(self):
        p, c = 1, 2
        
        item = self.heap[p]
        temp = self.heap[self.heap_size]
        self.heap_size -= 1
        
        while c <= self.heap_size:
            if c < self.heap_size and self.heap[c] > self.heap[c + 1]:
                c += 1
            if temp < self.heap[c]:
                break
            self.heap[p] = self.heap[c]
            p = c
            c *= 2
        
        self.heap[p] = temp
        self.heap.pop()
        return item
    
    def heapify(self, lst, idx, heapsize):
        l = idx * 2
        r = idx * 2 + 1
        
        s_idx = idx
        
        if l <= heapsize and lst[s_idx] > lst[l]:
            s_idx = l
        if r <= heapsize and lst[s_idx] > lst[r]:
            s_idx = r
        if s_idx != idx:
            lst[idx], lst[s_idx] = lst[s_idx], lst[idx]
            heapify(lst, s_idx, heapsize)
    
    
mh = Min_Heap()

prio = [100, 40, 50, 10, 15, 30, 60]

for i in prio:
    mh.insert_min_heap(i)

print(mh.heap)
print(mh.removed_key())
