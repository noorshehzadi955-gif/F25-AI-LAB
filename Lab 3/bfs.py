 1. BFS (Breadth-First Search)

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

start = "A"
goal = "F"

queue = deque([start])
visited = [start]

while queue:
    node = queue.popleft()

    print(node)

    # Goal check
    if node == goal:
        print("Goal found")
        break

    # Explore neighbours
    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)
