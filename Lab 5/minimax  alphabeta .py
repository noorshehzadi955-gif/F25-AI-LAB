"""
Lab 5: Adversarial Search - Minimax & Alpha-Beta Pruning
Course : CAI601400 - Artificial Intelligence
Purpose: Implement Minimax and Alpha-Beta pruning on a complete binary
         game tree, count the evaluated leaf nodes, and compare both
         algorithms to show that pruning reduces work without changing
         the final Minimax decision.
"""

import math


# ----------------------------------------------------------------------
# Minimax (with leaf-evaluation counter)
# ----------------------------------------------------------------------
def minimax(depth, index, max_turn, scores, target, counter):
    """
    Plain Minimax on a complete binary tree stored as a flat list of leaves.

    depth    : current depth in the tree (root = 0)
    index    : index of the current node within its level
    max_turn : True if it is MAX's turn, False if it is MIN's turn
    scores   : list of terminal (leaf) utilities
    target   : depth at which the leaves are located
    counter  : one-element list used as a mutable leaf counter
    """
    # Base case: a leaf has been reached, so return its utility
    if depth == target:
        counter[0] += 1
        return scores[index]

    # MAX layer: choose the child with the highest value
    if max_turn:
        return max(
            minimax(depth + 1, index * 2,     False, scores, target, counter),
            minimax(depth + 1, index * 2 + 1, False, scores, target, counter),
        )

    # MIN layer: choose the child with the lowest value
    return min(
        minimax(depth + 1, index * 2,     True, scores, target, counter),
        minimax(depth + 1, index * 2 + 1, True, scores, target, counter),
    )


# ----------------------------------------------------------------------
# Alpha-Beta pruning (with leaf-evaluation counter)
# ----------------------------------------------------------------------
def alphabeta(depth, index, max_turn, scores, target, alpha, beta, counter):
    """
    Minimax with alpha-beta pruning.

    alpha : best value MAX can guarantee so far along the current path
    beta  : best value MIN can guarantee so far along the current path
    Pruning condition: alpha >= beta (remaining siblings cannot change
    the final decision, so they are skipped).
    """
    # Base case: a leaf has been reached, so return its utility
    if depth == target:
        counter[0] += 1
        return scores[index]

    if max_turn:
        # MAX layer: start with the worst possible value
        value = float('-inf')
        for i in range(2):
            value = max(
                value,
                alphabeta(depth + 1, index * 2 + i, False,
                          scores, target, alpha, beta, counter),
            )
            alpha = max(alpha, value)      # update MAX's guaranteed bound
            if alpha >= beta:              # pruning: MIN above will never allow this branch
                break
        return value

    # MIN layer: start with the worst possible value for MIN
    value = float('inf')
    for i in range(2):
        value = min(
            value,
            alphabeta(depth + 1, index * 2 + i, True,
                      scores, target, alpha, beta, counter),
        )
        beta = min(beta, value)            # update MIN's guaranteed bound
        if alpha >= beta:                  # pruning: MAX above will never choose this branch
            break
    return value


# ----------------------------------------------------------------------
# Comparison helper
# ----------------------------------------------------------------------
def compare(name, scores):
    """Run both algorithms on the same tree and print value and leaf count."""
    scores = list(scores)                  # copy so the caller's list is not modified

    # Tree depth needed to hold all leaves
    depth = math.ceil(math.log2(len(scores)))

    # Pad with zeros so the tree is a complete binary tree
    scores += [0] * (2 ** depth - len(scores))

    minimax_leaves = [0]
    alphabeta_leaves = [0]

    minimax_value = minimax(0, 0, True, scores, depth, minimax_leaves)
    alphabeta_value = alphabeta(0, 0, True, scores, depth,
                                float('-inf'), float('inf'), alphabeta_leaves)

    print(f"{name:<22} scores={scores}")
    print(f"{'':<22} Minimax value={minimax_value}, leaves={minimax_leaves[0]} | "
          f"AlphaBeta value={alphabeta_value}, leaves={alphabeta_leaves[0]} | "
          f"Same? {minimax_value == alphabeta_value}\n")


# ----------------------------------------------------------------------
# Driver code
# ----------------------------------------------------------------------
if __name__ == "__main__":
    compare("5.1 supplied tree", [3, 5, 2, 9, 0, 7])
    compare("5.2 supplied tree", [3, 5, 2, 9, 3, 5, 2, 9])
    compare("Reorder 1",         [9, 5, 3, 2, 9, 5, 3, 2])
    compare("Reorder 2",         [2, 3, 5, 9, 2, 3, 5, 9])
    compare("Edge: all equal",   [4, 4, 4, 4, 4, 4, 4, 4])