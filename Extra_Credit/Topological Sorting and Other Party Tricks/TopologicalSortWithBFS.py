def topologicalBFS(start, graph):
    q = [start]
    stack = []
    while q:
        node = q.pop(0)
        if node not in stack:
            stack.append(node)

            if node in graph:
                for neighbor in graph[node]:
                    q.append(neighbor)

    return stack

graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6'],
    '4': ['7'],
    '5': ['7'],
    '6': ['5'],
    '7': []
}
print(topologicalBFS('1', graph))
