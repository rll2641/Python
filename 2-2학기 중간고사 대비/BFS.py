from collections import deque

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def bfs(graph, start_node):
    need_visited, visited = deque([]), list()
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited.popleft()
        
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    
    return visited

print(bfs(graph, 'A'))