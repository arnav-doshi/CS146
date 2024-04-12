def topologicalSort(graph):
    stack = []
    visit = {}

    for node in graph:
        visit[node] = 0

    for node in graph:
        if visit[node] == 0:
            dfs(node, visit, graph, stack)
    
    sorted = []
    while stack:
        sorted.append(stack.pop())
    
    return sorted

def dfs(node, visit, graph, stack):
    visit[node] = 1
    for next in graph[node]:
        if visit[next] == 0:
            dfs(next, visit, graph, stack)
    stack.append(node)

graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6'],
    '4': ['7'],
    '5': ['7'],
    '6': ['5'],
    '7': []
}

print(topologicalSort(graph))
