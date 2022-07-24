nums = [1, 2, 3]

# dfs
def purmute(nums):
    results = []
    prev_elements = []
    
    def dfs(elemnts):
        if len(elemnts) == 0:
            results.append(prev_elements[:])
        
        for e in elemnts:
            next_elements = elemnts[:]
            next_elements.remove(e)
            
            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()
            
    dfs(nums)
    return results

result = purmute(nums)
print(result)

# itertool
from itertools import permutations
def permute_iter(nums):
    return list(map(list, permutations(nums)))
print(permute_iter(nums))
