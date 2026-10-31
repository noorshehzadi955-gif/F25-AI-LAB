graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

start = 'A'
goal = 'G'

stack = [start]
visited = []

while stack:
    node = stack.pop()

    if node not in visited:
        visited.append(node)
        print(node)

        if node == goal:
            print("Goal found:", node)
            break

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)