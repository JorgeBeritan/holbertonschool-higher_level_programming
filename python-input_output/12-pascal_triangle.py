#!/usr/bin/python3

def pascal_triangle(n):
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
