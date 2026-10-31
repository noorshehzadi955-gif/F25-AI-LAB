from dls import dls


def iddfs(start, goal, max_depth):

    for limit in range(max_depth + 1):

        status, path = dls(start, goal, limit, [start])

        print("Depth limit:", limit)
        print("Status:", status)
        print("Path:", path)
        print()

        if status == "FOUND":
            return path

    return None


start = 'A'
goal = 'G'

print("IDDFS Results")

final_path = iddfs(start, goal, 4)

print("Final path:", final_path)