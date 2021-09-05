def dfs(node):
    if node not in visited:
        visited.append(node)
        print(node + ' ')
        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour) 



graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': ['a'],
    'f': [],
}

visited = []

for node in graph:
    if node not in visited:
        dfs(node)