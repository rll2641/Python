graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}
# 재귀
def dfs_recursion(v, visited = []):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            visited = dfs_recursion(w, visited)
    return visited

# 스택
def dfs_stack(v, visited = []):
    stack = [v]
    visited.append(v)
    
    while stack:
        v = stack.pop()
        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                stack.append(i)
    return visited