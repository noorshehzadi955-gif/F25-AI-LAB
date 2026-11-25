import heapq

# Graph
graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

# Heuristic Values
heuristic = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0
}

start = "S"
goal = "G"


# A* Search Algorithm
def astar(graph, heuristic, start, goal):

    queue = [(heuristic[start], 0, start, [start])]
    cost = {start: 0}

    processed = []
    expanded = 0

    while queue:

        f_cost, path_cost, node, path = heapq.heappop(queue)

        if path_cost != cost[node]:
            continue

        processed.append(node)

        if node == goal:
            return path_cost, path, processed, expanded

        expanded += 1

        for neighbour, edge_cost in graph[node]:

            new_cost = path_cost + edge_cost

            if neighbour not in cost or new_cost < cost[neighbour]:

                cost[neighbour] = new_cost

                f_cost = new_cost + heuristic[neighbour]

                heapq.heappush(
                    queue,
                    (f_cost, new_cost, neighbour, path + [neighbour])
                )

    return None, [], processed, expanded


# Display Results
def show_result(title, result):

    path_cost, path, processed, expanded = result

    print("\n" + title)
    print("Path:", path)
    print("Total Cost:", path_cost)
    print("Processed Nodes:", processed)
    print("Expanded Nodes:", expanded)


# TASK 1: A* Search
print(" TASK 1: A* SEARCH ")

astar_result = astar(graph, heuristic, start, goal)

show_result("A* Results", astar_result)


# TASK 2: UCS Comparison
print("\n TASK 2: UCS SEARCH ")

zero_heuristic = {
    "S": 0,
    "A": 0,
    "B": 0,
    "C": 0,
    "G": 0
}

ucs_result = astar(graph, zero_heuristic, start, goal)

show_result("UCS Results", ucs_result)


# TASK 3: Overestimated Heuristic
print("\nTASK 3: OVERESTIMATED HEURISTIC ")

modified_heuristic = heuristic.copy()

modified_heuristic["C"] = 10

print("Original h(C):", heuristic["C"])
print("Modified h(C):", modified_heuristic["C"])

overestimate_result = astar(
    graph, modified_heuristic, start, goal
)

show_result("Overestimated A* Results", overestimate_result)
