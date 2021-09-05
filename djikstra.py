def getMinNode():
    minNode = None
    minValue = float('inf')
    for v in dist:
        if dist[v] < minValue and visited[v] == False:
            minNode = v
            minValue = dist[v]

    return minNode

def checkIfAllVisited():
    for value in visited:
        if visited[value] == True:
            continue
        else:
            return False
    return True

def makeRelaxation(node):
    for neighbour, weight in graph[node]:
        if dist[neighbour] > dist[node] + weight:
            dist[neighbour] = dist[node] + weight
    
graph = {
    1: [(2, 2), (3, 4)],
    2: [(3, 1), (4, 7)],
    3: [(5, 3)],
    4: [(6, 1)],
    5: [(4, 2), (6, 5)],
    6: [],
}
src = 1
dest = 6

dist = {}

for node in graph:
    if node not in dist:
        dist[node] = float('inf')
dist[src] = 0

visited = {}
for vertex in graph:
    visited[vertex] = False


while not checkIfAllVisited():
    node = getMinNode()
    visited[node] = True
    makeRelaxation(node)

print(dist)
print(dist[dest])
    
