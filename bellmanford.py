graph = {
    'A': [['B', -1], ['C', 4]],
    'B': [['C', 3], ['D', 2], ['E', 2]],
    'C': [],
    'D': [['B', 1], ['C', 5]],
    'E': [['D', -3]]
}

# graph = {
#     1: [(2, 2), (3, 4)],
#     2: [(3, 1), (4, 7)],
#     3: [(5, 3)],
#     4: [(6, 1)],
#     5: [(4, 2), (6, 5)],
#     6: [],
# }


src = "A"
newGraph = {}
n = len(graph)

for node in graph:
    if node == src:
        newGraph[node] = 0
        for neighbour, weight in graph[node]:
            newGraph[neighbour] = weight
    else:
        if node not in newGraph:
            newGraph[node] = float('inf')

for i in range(n):
    for node in graph:
        for neighbour, weight in graph[node]:
            if newGraph[neighbour] > newGraph[node] + weight:
                newGraph[neighbour] = newGraph[node] + weight

print(newGraph)