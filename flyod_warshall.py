graph = {
    0: [[1, 5], [3, 10]],
    1: [[2, 3]],
    2: [[3, 1]],
    3: []
}


newGraph = []
n = len(graph)
for node in graph:
    l = [float('inf')] * n
    l[node] = 0
    for neighbour, weight in graph[node]:
        l[neighbour] = weight
    newGraph.append(l)

print(newGraph)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if newGraph[i][j] > newGraph[i][k] + newGraph[k][j]:
                newGraph[i][j] = newGraph[i][k] + newGraph[k][j]

print(newGraph)
