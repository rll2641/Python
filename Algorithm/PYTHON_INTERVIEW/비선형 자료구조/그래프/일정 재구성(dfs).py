from collections import defaultdict

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
graph, route = defaultdict(list), []

for a, b in sorted(tickets):
    graph[a].append(b)
    
def dfs(a):
    while graph[a]:
        dfs(graph[a].pop(0))
    route.append(a)

dfs('JFK')

print(route[::-1])

# 스택
def findItinerary(tickets):
    graph = defaultdict(list)
    
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)
    
    route = []
    
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)
    
    dfs('JFK')
    return route
