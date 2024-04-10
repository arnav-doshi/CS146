def reverseGraphEdges(graph):
    reverse = {}
    for u in graph:
        next = graph[u]
        for v in next:
            if v not in reverse:
                reverse[v] = []
            reverse[v].append(u)
    return reverse

graph = {
    '1': ['2', '5'],
    '2': ['1'],
    '3': ['2'],
    '4': ['1', '5'],
    '5': ['3']
}

reverse = reverseGraphEdges(graph)
for vertex in reverse:
    neighbors = reverse[vertex]
    print(str(vertex) + ": " + str(neighbors))