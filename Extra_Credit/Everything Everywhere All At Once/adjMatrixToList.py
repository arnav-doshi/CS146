def adjMatrixToList(adjMatrix):
    adjList = []
    for i in range(len(adjMatrix)):
        neighbors = []
        for j in range(len(adjMatrix[i])):
            if adjMatrix[i][j] != 0:
                neighbors.append(j + 1)
        adjList.append(neighbors)

    return adjList

adjMatrix = [
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0]
]

adjList = adjMatrixToList(adjMatrix)

for i in range(len(adjList)):
    nexts = adjList[i]
    print(str(i + 1) + ": " + str(nexts))
