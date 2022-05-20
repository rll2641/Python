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
        data = self.heap[self.heap_size]
        
        while c <= self.heap_size:
            if c < self.heap_size and self.heap[c] > self.heap[c + 1]:
                c += 1
            if data < self.heap[c]:
                break
            self.heap[p] = self.heap[c]
            p = c
            c *= 2
        
        self.heap[p] = data
        self.heap.pop()
        return item

mh = Min_Heap()

prio = [10, 40, 50, 15, 30, 100, 60]

for i in prio:
    mh.insert_min_heap(i)
    
print(mh.heap)
print("")
print(mh.removed_key())
print("")
print(mh.heap)