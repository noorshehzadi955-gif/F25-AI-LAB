# 1. BFS (Breadth-First Search)
from collections import deque

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

queue = deque([start])
visited = []

while queue:
    node = queue.popleft()

    if node not in visited:
        visited.append(node)
        print(node)

        if node == goal:
            print("Goal found:", node)
            break

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)