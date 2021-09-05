# Given list of graphs return the largest connected graph

def dfs(node, count):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                count += dfs(neighbour, 1)
        return count
    else:
        return 0

graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}

visited = []
maxLength = float('-inf')
for node in graph:
    if node not in visited:
        maxLength = max(maxLength, dfs(node, 1))

print('MaxLength:', maxLength)