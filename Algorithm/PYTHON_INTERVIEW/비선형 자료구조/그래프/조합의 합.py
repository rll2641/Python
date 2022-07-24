candidates = [2, 3, 6, 7]
target = 7

result = []

def dfs(csum, index, path):
    if csum < 0:
        return
    if csum == 0:
        result.append(path)
    
    for i in range(index, len(candidates)):
        dfs(csum - candidates[i], i, path + [candidates[i]])
    
    return result

print(dfs(target, 0, []))