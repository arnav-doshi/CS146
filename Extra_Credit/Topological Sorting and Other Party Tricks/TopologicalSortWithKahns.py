def topological_sort(graph):
    inDegree = {}

    for node in graph:
        inDegree[node] = 0

    for node in graph:
        for nextN in graph[node]:
            if nextN not in inDegree:
                inDegree[nextN] = 0
            inDegree[nextN] += 1
    
    queue = []
    for node in graph:
        if inDegree[node] == 0:
            queue.append(node)


    result = []
    front = 0
    
    doneNodes = 0
    while front < len(queue):
        node = queue[front]
        result.append(node)
        front += 1
        doneNodes += 1
        for nextN in graph[node]:
            inDegree[nextN] -= 1

            if inDegree[nextN] == 0:
                queue.append(nextN)


    return result


graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6'],
    '4': ['7'],
    '5': ['7'],
    '6': ['5'],
    '7': []
}

print(topological_sort(graph)) 
