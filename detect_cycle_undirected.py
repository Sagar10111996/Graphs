def dfs(node, parent):
    visited[node] = True
    for neighbour in graph[node]:
        if neighbour == parent:
            continue
        elif visited[neighbour] == True:
            return True
        else:
            dfs(neighbour, node)

    return False


graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'A']
}

visited = {}

for node in graph:
    visited[node] = False

for node in graph:
    if visited[node] == False:
        if dfs(node, None):
            print('Has cycles')
            break
else:
    print('Does not have cycles')
