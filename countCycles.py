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

graph = {
    1: [3],
    2: [1, 5],
    3: [4],
    4: [2],
    5: [7],
    6: [5],
    7: [8],
    8: [6]
}

visited = {}
recursion = {}

for node in graph:
    visited[node] = False
    recursion[node] = False

for node in graph:
    if visited[node] == False:
        if dfs(node):
            print('Detected Cycle')
