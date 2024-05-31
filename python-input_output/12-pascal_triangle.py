#!/usr/bin/python3
"""Made by Jorge Beritan
"""

def pascal_triangle(n):
    """In this function we learn about made an algorithm to make a Pascal Triangle
    """
    x = []
    y = []

    for i in range(n):
        z = x[:]
        z.append(1)
        position = len(x)
        for i  in range(1, position):
            z[i] = x[i - 1] + x[i]
        x = z[:]
        y.append(x)
    return y
