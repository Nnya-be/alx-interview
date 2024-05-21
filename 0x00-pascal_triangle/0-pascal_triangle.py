#!/usr/bin/python3
"""
pascal_triangle - function that computes and returns the pascal's triangle.
n(int) - The number of rows to be printed.
return - A list of lists that contains the pascal's triangle.
"""
def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = []
    for row_num in range(n):
        row = [1]
        if triangle:
            prev = triangle[-1]
            for num in range(1, len(prev)):
                row.append(prev[num - 1] + prev[num])
            row.append(1)
            triangle.append(row)
        else:
            triangle.append([1])
            
    return triangle
