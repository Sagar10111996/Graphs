graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': ['a'],
    'f': [],
}


visited = []

queue = ['a']

while len(queue) > 0:
    node = queue.pop(0)
    visited.append(node)
    print(node, end=" ")
    for neighbour in graph[node]:
        if neighbour not in visited:
            queue.append(neighbour)

