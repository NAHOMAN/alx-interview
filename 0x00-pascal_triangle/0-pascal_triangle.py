#!/usr/bin/python3

def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    triangle = []  # This will hold the rows of Pascal's triangle

    for i in range(n):
        # Initialize the current row with 1s
        row = [1] * (i + 1)

        # Calculate the values for the inner elements of the row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)  # Add the constructed row to the triangle

    return triangle
