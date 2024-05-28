#!/usr/bin/python3
"""By me
"""


import json


def load_from_json_file(filename):
    """In this function we can learn how create an objecto from a json file
    """
    with open(filename, "r", encoding="utf-8") as archive:
        extract = archive.read()
        load = json.loads(extract)
    return load
