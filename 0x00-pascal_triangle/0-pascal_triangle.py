#!/usr/bin/python3

def pascal_triangle(n):
    """ Returns a list of lists representing Pascal's triangle of size n. """

    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Initialize the current row with 1s
        row = [1] * (i + 1)

        # Calculate the values for the current row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Append the current row to the triangle
        triangle.append(row)

    return triangle
