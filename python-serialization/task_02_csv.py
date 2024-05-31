#!/usr/bin/python3
"""Made by Jorge Beritan
"""

import csv
import json


def convert_csv_to_json(filename):
    """In this function we learn how cconvert a csv to json
    """
    try:
        with open(filename, "r") as archive:
            csv_reader = csv.DictReader(archive)
            data = [row for row in csv_reader]

        with open("data.json", "w") as archive:
            archive.write(json.dumps(data))
        return True
    except FileNotFoundError:
        return False
