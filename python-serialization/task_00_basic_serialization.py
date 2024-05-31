#!/usr/bin/python3
"""Made by Jorge Beritan
"""


import json


def serialize_and_save_to_file(data, filename):
    """In this function we can get a data and serialize to a file
    """
    with open(filename, "w", encoding="utf-8") as archive:
        archive.write(json.dumps(data))
    

def load_and_deserialize(filename):
    """In this function  we can get a file and desrealize
    """
    with open(filename, "r") as archive:
        extract = archive.read()
        load = json.loads(extract)
    return load
