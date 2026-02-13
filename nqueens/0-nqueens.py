#!/usr/bin/python3
"""N Queens puzzle solver.

Usage: nqueens N
"""
import sys


def solve_nqueens(n):
    """Generate all solutions for N-Queens as lists of [row, col] pairs."""
    cols = set()
    pos_diag = set()  # r + c
    neg_diag = set()  # r - c
    board = [0] * n
    solutions = []

    def backtrack(r=0):
        if r == n:
            sol = [[i, board[i]] for i in range(n)]
            solutions.append(sol)
            return

        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r] = c

            backtrack(r + 1)

            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)

    backtrack(0)
    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    for sol in solve_nqueens(n):
        print(sol)


if __name__ == '__main__':
    main()
