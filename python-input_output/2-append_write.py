#!/usr/bin/python3
"""In this function we learn abbout to create a new file and write in here
"""


def append_write(filename="", text=""):
    """In this function we open a file with w and append a string"""
    with open(filename, "w", encoding="utf-8") as archive:
        archive.append(text)
    return len(text)
