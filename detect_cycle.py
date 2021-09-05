# Detect cycle in directed graph

def dfs(node):
    visited[node] = True
    recursion[node] = True
    for neighbour in graph[node]:
        if visited[neighbour] == False:
            if dfs(neighbour):
                return True
        elif recursion[neighbour] == True:
            return True
    recursion[node] = False
    return False

# graph = {
#     1: [2],
#     2: [],
#     4: [1, 5],
#     5: [6],
#     6: [4]
# }
graph = {
    1: [2],
    2: [3],
    3: []
}

visited = {}
recursion = {}

for vertex in graph:
    visited[vertex] = False
    recursion[vertex] = False


for node in graph:
    if visited[node] == False:
        if dfs(node):
            print('Has Cycles')
            break
else:
    print('No cycles')