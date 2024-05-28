#!/usr/bin/python3
"""By me
"""


import json


def save_to_json_file(my_obj, filename):
    """In this function we represent a json write in a archive
    """
    with open(filename, "w") as archive:
        archive.write(json.dumps(my_obj))
