#!/usr/bin/python3
"""Function for indentation a text
"""


def text_indentation(text):
    """Implement a few border case
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n").replace(":", ":\n\n")
    text = text.replace("?", "?\n\n").replace("\n ", "\n")
    text = text.replace("   ", "")
    print(text, end="")
