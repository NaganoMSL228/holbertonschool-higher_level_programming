#!/usr/bin/python3
"""
N Queens Solver

This module solves the N Queens problem, placing N non-attacking queens
on an N×N chessboard.
"""

import sys


def is_safe(board, row, col, n):
    """
    Determine if placing a queen at board[row][col] is safe.

    Args:
        board (list): Current state of the chessboard.
        row (int): Row index for the queen.
        col (int): Column index for the queen.
        n (int): Size of the board.

    Returns:
        bool: True if safe, False otherwise.
    """
    # Check for queens in the same row to the left
    if any(board[row][i] == 1 for i in range(col)):
        return False

    # Check upper diagonal on the left
    for i in range(row, -1, -1):
        if board[i][col] == 1:
            return False

    # Check lower diagonal on the left
    for i in range(row, n):
        if board[i][col] == 1:
            return False

    return True


def solve_nqueens(board, col, n, solutions):
    """
    Recursively find all solutions to the N Queens problem.

    Args:
        board (list): Current state of the chessboard.
        col (int): Current column being processed.
        n (int): Size of the board.
        solutions (list): List to store found solutions.

    Returns:
        None
    """
    # If all queens are placed successfully
    if col >= n:
        solution = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 1]
        solutions.append(solution)
        return

    # Try placing a queen in each row of the current column
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen
            solve_nqueens(board, col + 1, n, solutions)  # Recur to place next queen
            board[row][col] = 0  # Backtrack


def nqueens(n):
    """
    Solve and print all solutions for N Queens.

    Args:
        n (int): Size of the board and number of queens.

    Returns:
        None
    """
    # Validate input
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard
    board = [[0] * n for _ in range(n)]
    solutions = []
    
    solve_nqueens(board, 0, n, solutions)

    # Print all found solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    """Entry point of the program."""
    
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
