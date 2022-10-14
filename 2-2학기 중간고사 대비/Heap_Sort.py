def heapify(lst, idx, heapsize):
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

def heap_sort(lst):
    
    n = len(lst)
    for i in range(n, 0, -1):
        heapify(lst, 1, i-1)
        
prio = [0, 5, 3, 4, 2, 1]

heap_sort(prio)
print(prio)