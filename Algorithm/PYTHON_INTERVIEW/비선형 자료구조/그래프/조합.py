def combine(n, k):
    results = []
    
    def dfs(elements, start, k):
        if k == 0:
            results.append(elements[:])
            return
    
        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()
        
    dfs([], 1, k)
    return results

print(combine(4,2))

# itertools
from itertools import combinations
n, k = 4, 2
def combine_iter(n, k):
    return list(combinations(range(1, n+1), k))
print(combine(n, k))