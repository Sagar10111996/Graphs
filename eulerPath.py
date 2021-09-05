edges = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]


def checkIfPathExists():
    inFlag = 0
    outFlag = 0
    for node in graph:
        if incoming[node] == outgoing[node]:
            continue
        elif incoming[node] > outgoing[node]:
            inFlag += 1
        elif outgoing[node] > incoming[node]:
            outVertex = node
            outFlag += 1

    if inFlag < 2 and outFlag < 2:
        return True, outVertex


graph = {}
incoming = {}
outgoing ={}

for at, to in edges:
    if at not in graph:
        graph[at] = []
    graph[at].append(to)
    if to not in graph:
        graph[to] = []

for node in graph:
    if node not in outgoing:
        outgoing[node] = 0
    outgoing[node] = len(graph[node])
    for neighbour in graph[node]:
        if neighbour not in incoming:
            incoming[neighbour] = 0
        incoming[neighbour] += 1

def dfs(outvertex):
    while outgoing[outvertex] > 0:
        outgoing[outvertex] -= 1
        neighbour = graph[outvertex].pop(0)
        dfs(neighbour)
    path.append(outvertex)


pathExists, outvertex = checkIfPathExists()
path = []
if pathExists:
    dfs(outvertex)
    print('Path:', path)
else:
    print('Path does not exist')
