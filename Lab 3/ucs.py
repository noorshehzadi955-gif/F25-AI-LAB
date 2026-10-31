
import heapq

graph = {
    'A': [('B', 1), ('C', 6)],
    'B': [('D', 4), ('E', 1)],
    'C': [('F', 3), ('G', 6)],
    'D': [],
    'E': [('G', 1)],
    'F': [],
    'G': []
}

start = 'A'
goal = 'G'

queue = [(0, start)]
cost = {start: 0}
parent = {start: None}
visited = []

while queue:
    path_cost, node = heapq.heappop(queue)

    if node in visited:
        continue

    visited.append(node)
    print("Visited node:", node)
    print("Path cost:", path_cost)

    if node == goal:
        print("Goal found:", node)
        print("Total cost:", path_cost)

        path = []
        current = node

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()
        print("Final path:", path)
        break

    for neighbour, edge_cost in graph[node]:
        new_cost = path_cost + edge_cost

        if neighbour not in cost or new_cost < cost[neighbour]:
            cost[neighbour] = new_cost
            parent[neighbour] = node
            heapq.heappush(queue, (new_cost, neighbour))
