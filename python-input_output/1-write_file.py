#!/usr/bin/python3
"""In this function we learn about write in a text file
"""


def write_file(filename="", text=""):
    """In this function we implement a with reserveted word write in a file
    """
    with open(filename, "w", encoding="utf-8") as archive:
        archive.write(text)
    archive.close()
    return len(text)
