graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}


def dls(node, goal, limit, path):

    if node == goal:
        return "FOUND", path

    if limit == 0:
        if graph[node]:
            return "CUTOFF", None
        return "FAILURE", None

    cutoff_found = False

    for neighbour in graph[node]:

        if neighbour not in path:

            status, result = dls(
                neighbour, goal, limit - 1, path + [neighbour]
            )

            if status == "FOUND":
                return status, result

            if status == "CUTOFF":
                cutoff_found = True

    if cutoff_found:
        return "CUTOFF", None

    return "FAILURE", None


start = 'A'
goal = 'G'

for limit in range(1, 5):

    status, path = dls(start, goal, limit, [start])

    print("Limit:", limit)
    print("Status:", status)
    print("Path:", path)
    print()