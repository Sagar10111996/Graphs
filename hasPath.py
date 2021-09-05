def has_path_dfs(src, dest):
    if src not in visited:
        visited.append(src)
        if src == dest:
            return True
        for neighbour in graph[src]:
            if has_path_dfs(neighbour, dest):
                return True
        return False

def has_path_bfs(src, dest):
    queue = [src]
    while len(queue) > 0:
        node = queue.pop(0)
        visited.append(node)
        if node == dest:
            return True
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

    return False

graph = {
    'f': ['g', 'i'],
    'i': ['g', 'k'],
    'j': ['i'],
    'g': ['h'],
    'h': [],
    'k': []
}

visited = []
print(has_path_dfs('f', 'h'))
visited = []
print(has_path_bfs('f', 'j'))