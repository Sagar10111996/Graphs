def dfs(node):
    visited.append(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour)
    current_order.append(node)


graph = {
    3: [1],
    2: [3],
    5: [2, 0],
    1: [],
    0: [],
    4: [0, 1],
}

visited = []
current_order = []
topo_order= []
for node in graph:
    if node not in visited:
        current_order = []
        dfs(node)
        for ele in current_order:
            topo_order.insert(0, ele)

print(topo_order)
