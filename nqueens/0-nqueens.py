#!/usr/bin/python3
"""N queens problem solver.

Usage: nqueens N

Prints all possible solutions for an N x N board.
Only the `sys` module is used as required.
"""

import sys


def solve_nqueens(n):
    """Generate all solutions for the N-Queens problem.

    Each solution is a list of [row, col] pairs.
    """
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col
    board = []
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append([[r, c] for r, c in board])
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board.append((row, col))

            backtrack(row + 1)

            board.pop()
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    arg = sys.argv[1]
    try:
        n = int(arg)
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    for sol in solve_nqueens(n):
        print(sol)


if __name__ == "__main__":
    main()
