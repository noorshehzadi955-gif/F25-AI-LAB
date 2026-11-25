import heapq

start = 'A'
goal = 'G'

queue = [(0, start)]
cost = {start: 0}

while queue:
    path_cost, node = heapq.heappop(queue)

    if path_cost > cost[node]:
        continue

    if node == goal:
        print("Goal visited:", node)
        print("Total cost:", path_cost)
        break

    for neighbour, edge_cost in graph[node]:
        new_cost = path_cost + edge_cost

        if neighbour not in cost or new_cost < cost[neighbour]:
            cost[neighbour] = new_cost
            heapq.heappush(queue, (new_cost, neighbour))
