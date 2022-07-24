nums = [1, 2, 3]
result = []
def dfs(index, path):
    result.append(path)
    
    for i in range(index, len(nums)):
        dfs(i + 1, path + [nums[i]])
    return result
print(dfs(0, []))