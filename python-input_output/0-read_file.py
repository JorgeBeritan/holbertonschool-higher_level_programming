#!/usr/bin/python3
"""In this fucntion we learn how we open a file
"""


def read_file(filename=""):
    """In this function we open a file and print the content
    """
    with open(filename, "r", encoding="ustf-8") as line:
        mostrar = line.read()
    print(mostrar)
    line.close()
