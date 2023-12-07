#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    A function that returns a list
    of integers representing the
    Pascal triangle of n:
       . Returns an empty list if n <= 0
       . Assume n will always be an integer
    """
    # Initialize an empty list to store Pascal's Triangle
    pascal_triangle_list = []

    # Check if n is less than or equal to 0, return an empty list
    if n <= 0:
        return []

    # Iterate through each row in Pascal's Triangle up to the given n
    for i in range(n):
        # For the first row, append [1] to the Pascal's Triangle list
        if i == 0:
            pascal_triangle_list.append([1])
        else:
            # For subsequent rows, calculate each element in the row
            current_row = []
            for j in range(i + 1):
                # The first and last elements in each row are always 1
                if j == 0 or j == i:
                    current_row.append(1)
                else:
                    # Calculate the middle elements using the values
                    # from the previous row
                    current_row.append(pascal_triangle_list[i - 1][j - 1] +
                                       pascal_triangle_list[i - 1][j])

            # Append the current row to the Pascal's Triangle list
            pascal_triangle_list.append(current_row)

    # Return the final Pascal's Triangle list
    return pascal_triangle_list
