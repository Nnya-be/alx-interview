#!/usr/bin/python3
"""
pascal_triangle - function that computes and returns the pascal's triangle.
n(int) - The number of rows to be printed.
return - A list of lists that contains the pascal's triangle.
"""
def pascal_triangle(n):
    if n <= 0:
        return []
