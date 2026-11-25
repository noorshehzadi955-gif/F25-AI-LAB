# Minimax and Alpha-Beta Pruning

values = [3, 5, 2, 9, 3, 5, 2, 9]

mini_count = 0
alpha_count = 0


# Minimax Function
def minimax(values, index, is_max):

    global mini_count

    # Leaf Node
    if index >= 4:
        mini_count += 1
        return values[index - 4]

    if is_max:
        left = minimax(values, index * 2 + 1, False)
        right = minimax(values, index * 2 + 2, False)
        return max(left, right)

    else:
        left = minimax(values, index * 2 + 1, True)
        right = minimax(values, index * 2 + 2, True)
        return min(left, right)


# Alpha-Beta Function
def alphabeta(values, index, is_max, alpha, beta):

    global alpha_count

    if index >= 4:
        alpha_count += 1
        return values[index - 4]

    if is_max:
        result = float('-inf')

        for child in [index * 2 + 1, index * 2 + 2]:
            result = max(result, alphabeta(
                values, child, False, alpha, beta
            ))

            alpha = max(alpha, result)

            if alpha >= beta:
                break

        return result

    else:
        result = float('inf')

        for child in [index * 2 + 1, index * 2 + 2]:
            result = min(result, alphabeta(
                values, child, True, alpha, beta
            ))

            beta = min(beta, result)

            if alpha >= beta:
                break

        return result


# Run Minimax
answer1 = minimax(values, 0, True)

# Run Alpha-Beta
answer2 = alphabeta(
    values, 0, True, float('-inf'), float('inf')
)

print("Minimax Value:", answer1)
print("Minimax Leaves:", mini_count)

print("Alpha-Beta Value:", answer2)
print("Alpha-Beta Leaves:", alpha_count)
