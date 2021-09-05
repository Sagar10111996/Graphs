def reverseGraph(graph):
    g = {}
    for node in graph:
        if node not in g:
            g[node] = []
        for neighbour in graph[node]:
            if neighbour not in g:
                g[neighbour] = []
            g[neighbour].append(node)

    return g

def dfs(g, visit, node):
    visit[node] = True
    for neighbour in g[node]:
        if neighbour not in visit:
            dfs(g, visit, neighbour)


# graph = {
#     1: [2, 3],
#     2: [5],
#     3: [5, 4],
#     4: [6],
#     5: [6, 7],
#     6: [8],
#     7: [8],
#     8: []
# }
graph = {
    1: [2, 3],
    2: [3],
    3: [4],
    4: []
}

visited1 = [False] * (len(graph)+1)
visited2 = [False] * (len(graph)+1)

newgraph = reverseGraph(graph)

dfs(graph, visited1, 1)
dfs(newgraph, visited2, 1)

print('V1:', visited1)
print('V2:', visited2)

for i in range(1, len(graph)+1):
    if visited1[i] == False and visited2[i] == False:
        print('Graph is not connected')
        break
else:
    print('Graph is connected')
