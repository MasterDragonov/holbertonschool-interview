#!/usr/bin/python3
"""This module defines a function that generates Pascal's Triangle."""


def pascal_triangle(n):
    """Generates a list of lists representing Pascal's triangle of size n.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists: Integers representing the triangle, or [] if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        prev_row = triangle[-1]
        # Start each row with a 1
        new_row = [1]

        # Calculate middle values based on the previous row
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])

        # End each row with a 1
        new_row.append(1)
        triangle.append(new_row)

    return triangle
