def adjacencyListToMatrix(adjList):
    nodeIndex = {}
    i = 0
    for node in adjList:
        nodeIndex[node] = i
        i += 1        
        
    adjMatrix = [[0] * len(adjList) for a in range(len(adjList))]

    for node in adjList:
        nodes = adjList[node]
        rowIndex = nodeIndex[node]
        
        for next in nodes:
            columnIndex = nodeIndex[next]
            adjMatrix[rowIndex][columnIndex] = 1
    
    return adjMatrix


adjList = {
    '1': ['2','4','5'],
    '2': ['1','3'],
    '3': ['2', '5'],
    '4': ['1', '5'],
    '5': ['1', '4', '3']
}

adjMatrix = adjacencyListToMatrix(adjList)

for r in adjMatrix:
    print(r)
